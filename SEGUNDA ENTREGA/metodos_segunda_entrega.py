import numpy as np

def sustprgr(L_b):
    n = L_b.shape[0]
    L = L_b[:, :-1]
    b = L_b[:, -1]
    z = np.zeros(n)
    for i in range(n):
        z[i] = (b[i] - np.dot(L[i, :i], z[:i])) / L[i, i]
    return z

def sustregr(U_z):
    n = U_z.shape[0]
    U = U_z[:, :-1]
    z = U_z[:, -1]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (z[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

def LU_simple(A, b):
    print("LU with simple gaussian elimination: \nResults: \n")
    A = np.array(A)
    b = np.array(b)
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    M = A.copy()

    print("Stage 0:")
    for row in M:
        print("  ".join(f"{element:8.6f}" for element in row))
    print("\n")
    for i in range(n-1):
        print(f"Stage: {i+1}")
        for j in range(i+1, n):
            if M[j, i] != 0:
                L[j, i] = M[j, i] / M[i, i]
                M[j, i:n] = M[j, i:n] - (M[j, i] / M[i, i]) * M[i, i:n]
        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]
        for row in M:
            print("  ".join(f"{element:8.6f}" for element in row))
        print("\n")
        print("L:")
        for row in L:
            print("  ".join(f"{element:8.6f}" for element in row))
        print("\n")
        print("U:")
        for row in U:
            print("  ".join(f"{element:8.6f}" for element in row))
        print("\n")
    U[n-1, n-1] = M[n-1, n-1]
    z = sustprgr(np.column_stack((L, b)))
    x = sustregr(np.column_stack((U, z)))
    
    print("After applying progressive and regressive substitution")
    print("\n")
    for i in x:
        print(i)

def LU_partial(A, b):
    print("LU with partial gaussian elimination: \nResults: \n")
    A = np.array(A)
    b = np.array(b)
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    P = np.eye(n)
    M = A.copy()
    
    print("Stage 0:")
    for row in M:
        print("  ".join(f"{element:8.6f}" for element in row))
    print("\n")

    for i in range(n-1):
        print(f"Stage: {i+1}")
        max_index = np.argmax(abs(M[i+1:n, i])) + i + 1
        if abs(M[max_index, i]) > abs(M[i, i]):
            M[[i, max_index], i:n] = M[[max_index, i], i:n]
            P[[i, max_index], :] = P[[max_index, i], :]

            if i > 0:
                L[[i, max_index], :i] = L[[max_index, i], :i]

        for j in range(i+1, n):
            if M[j, i] != 0:
                L[j, i] = M[j, i] / M[i, i]
                M[j, i:n] -= (M[j, i] / M[i, i]) * M[i, i:n]
        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]
        
        for row in M:
            print("  ".join(f"{element:8.6f}" for element in row))
        print("\n")
        print("L:")
        for row in L:
            print("  ".join(f"{element:8.6f}" for element in row))
        print("\n")
        print("U:")
        for row in U:
            print("  ".join(f"{element:8.6f}" for element in row))
        print("\n")
        print("P:")
        for row in P:
            print("  ".join(f"{element:8.6f}" for element in row))
        print("\n")
        
    U[n-1, n-1] = M[n-1, n-1]
    z = sustprgr(np.column_stack((L, np.dot(P, b))))
    x = sustregr(np.column_stack((U, z)))
    
    print("After applying progressive and regressive substitution")
    print("\n")
    for i in x:
        print(i)

def seidel(A, b, x0, tol, Nmax):
    print("Gauss-Seidel: \nResults: \n")
    A = np.array(A)
    b = np.array(b)
    xant = np.array(x0, dtype=float)
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    T = np.linalg.inv(D - L).dot(U)
    spectral_radius = np.max(np.abs(np.linalg.eigvals(T)))
    C = np.linalg.inv(D - L).dot(b)
    E = 1000
    cont = 0
    table = []
    
    print("T:")
    for row in T:
        print("  ".join(f"{element:8.6f}" for element in row))
    print("\n")
    print("C:")
    C_result = " ".join(str(i) for i in C)
    print(C_result)
    print("\n")
    print(f"Spectral radius: \n{spectral_radius}")
    print("\n")

    while E > tol and cont < Nmax:
        table.append([cont, "{:.5e}".format(E), xant.tolist()])
        xact = T.dot(xant) + C
        E = np.linalg.norm(xact - xant)
        xant = xact
        cont += 1
    table.append([cont, "{:.5e}".format(E), xant.tolist()])

    print("| {:^4} | {:^18} | {:^10} |".format("Iter", "E", "x"))
    for row in table:
        xant_str = " ".join(f"{val:8.6f}" for val in row[2])
        print("| {:<4} | {:<18} | {:<10} |".format(row[0], row[1], xant_str))
        
def SOR(A, b, x0, w, tol, Nmax):
    print("SOR(relaxation): \nResults: \n")
    A = np.array(A)
    b = np.array(b)
    xant = np.array(x0, dtype=float)

    D = np.diag(np.diag(A))
    L = -np.tril(A, -1) 
    U = -np.triu(A, 1)
    
    T = np.linalg.inv(D - w * L).dot((1 - w) * D + w * U)
    C = w * np.linalg.inv(D - w * L).dot(b)
    
    E = 1000
    cont = 0
    table = []

    while E > tol and cont < Nmax:
        xact = T.dot(xant) + C
        E = np.linalg.norm(xact - xant)
        xant = xact
        cont += 1
        
        table.append([cont, "{:.5e}".format(E), xant.tolist()])

    print("T:")
    for row in T:
        print("  ".join(f"{element:8.6f}" for element in row))
    print("\n")

    print("C:")
    C_result = " ".join(f"{i:8.6f}" for i in C)
    print(C_result)
    print("\n")

    print(f"Spectral radius: {np.max(np.abs(np.linalg.eigvals(T))):.6f}")
    print("\n")

    # Mostrar tabla de iteraciones
    print("| {:^4} | {:^18} | {:^10} |".format("Iter", "E", ""))
    for row in table:
        xant_str = " ".join(f"{val:8.6f}" for val in row[2])  # Convertir el vector a string
        print("| {:<4} | {:<18} | {:<10} |".format(row[0], row[1], xant_str))

A = [[4,-1,0,3], [1,15.5,3,8], [0,-1.3,-4,1.1], [14,5,-2,30]]
b = [1, 1, 1, 1]
x0 = [0, 0, 0, 0]
tol = 1e-7
N_max = 100
w = 1.5
   
LU_simple(A, b)
print("----------------------------------------------------------------------------------------------------------")
LU_partial(A, b)
print("----------------------------------------------------------------------------------------------------------")
seidel(A, b, x0, tol, N_max)
print("----------------------------------------------------------------------------------------------------------")
SOR(A, b, x0, w, tol, N_max)
print("----------------------------------------------------------------------------------------------------------")