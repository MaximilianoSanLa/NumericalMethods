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
def difdivididas(X, Y):
    # Convert X and Y to numpy arrays if they aren't already
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    
    n = len(X)
    D = np.zeros((n, n))  # Divided difference table

    # First column of the table is just the Y values
    D[:, 0] = Y

    # Compute the divided differences
    for j in range(1, n):
        for i in range(n - j):
            # Calculate each divided difference using the previous column
            D[i, j] = (D[i + 1, j - 1] - D[i, j - 1]) / (X[i + j] - X[i])

    # The coefficients of the Newton polynomial are the first row elements of each column
    Coef = D[0, :]

    # Output the divided difference table
    print("Tabla de diferencias divididas:")
    for row in D:
        print(" ".join(f"{x:.6f}" if x != 0 else "0.000000" for x in row))
    
    # Output the Newton coefficients
    print("\nCoeficientes del polinomio de Newton:")
    print(" ".join(f"{coef:.6f}" for coef in Coef))
    
    # Output the Newton polynomial
    print("\nPolinomio de Newton:")
    polynomial = f"{Coef[0]:.6f}"
    for i in range(1, len(Coef)):
        term = f"{Coef[i]:+.6f}"
        for k in range(i):
            term += f"(x-{X[k]:.6f})"
        polynomial += " " + term
    print(polynomial)
    
    return Coef

def lagrange(X, Y):
    # Convert X and Y to numpy arrays if they aren't already
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    
    n = len(X)
    L = np.zeros((n, n))  # Lagrange basis polynomials as rows

    # Construct Lagrange basis polynomials
    for i in range(n):
        # Exclude X[i] from the product terms
        aux0 = np.delete(X, i)
        aux = np.array([1.0])
        
        # Construct the polynomial L_i(x) for each i
        for xj in aux0:
            aux = np.convolve(aux, [1, -xj])  # Multiply by (x - xj)
        
        # Normalize L_i(x) so that L_i(X[i]) = 1
        L[i, :] = (aux / np.polyval(aux, X[i])).tolist() + [0] * (n - len(aux))

    # Compute coefficients of the interpolating polynomial by summing Lagrange terms
    Coef = Y @ L

    # Output Lagrange basis polynomials
    print("\nPolinomios interpolantes de Lagrange:")
    for i, row in enumerate(L):
        terms = " + ".join(f"{coef:.6f}x^{j}" for j, coef in enumerate(row[::-1]) if coef != 0)
        print(f"L{i}: {terms}")
    
    # Output interpolating polynomial
    polynomial = " + ".join(f"{Coef[i]:.6f}*L{i}" for i in range(n))
    print("\nPolinomio:")
    print(polynomial)
    
    return L, Coef


def trazlin(X, Y):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    n = len(X)
    m = 2 * (n - 1)
    A = np.zeros((m, m))
    b = np.zeros(m)

    # Interpolation conditions
    for i in range(n - 1):
        A[i, 2 * i:2 * i + 2] = [X[i + 1], 1]
        b[i] = Y[i + 1]
    A[n - 1, 0:2] = [X[0], 1]
    b[n - 1] = Y[0]

    # Continuity conditions
    for i in range(1, n - 1):
        A[n - 1 + i, 2 * i - 2:2 * i + 2] = [X[i], 1, -X[i], -1]
        b[n - 1 + i] = 0

    # Print matrix A and vector b for inspection
    print("Matrix A:\n", A)
    print("Vector b:\n", b)

    # Solve the system
    try:
        Saux = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        print("Error: Singular matrix detected.")
        return None

    # Organize output coefficients
    Coef = np.zeros((n - 1, 2))
    for i in range(n - 1):
        Coef[i, :] = Saux[2 * i:2 * i + 2]

    # Print the tracers for debugging
    print("\nCoeficientes de los trazadores lineales:")
    for i, (a, b) in enumerate(Coef):
        print(f"{a:.6f}x + {b:.6f}")

    return Coef

def trazcuad(X, Y):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    n = len(X)
    m = 3 * (n - 1)
    A = np.zeros((m, m))
    b = np.zeros(m)

    # Interpolation conditions
    for i in range(n - 1):
        A[i, 3 * i:3 * i + 3] = [X[i + 1]**2, X[i + 1], 1]
        b[i] = Y[i + 1]
    A[n - 1, 0:3] = [X[0]**2, X[0], 1]
    b[n - 1] = Y[0]

    # Continuity conditions
    for i in range(1, n - 1):
        A[n - 1 + i, 3 * i - 3:3 * i + 3] = [X[i]**2, X[i], 1, -X[i]**2, -X[i], -1]
        b[n - 1 + i] = 0

    # Smoothness conditions
    for i in range(1, n - 1):
        A[2 * (n - 1) - 1 + i, 3 * i - 3:3 * i + 3] = [2 * X[i], 1, 0, -2 * X[i], -1, 0]
        b[2 * (n - 1) - 1 + i] = 0

    # Boundary condition for the quadratic spline (second derivative zero at endpoints)
    A[-1, 0] = 2
    b[-1] = 0

    # Print matrix A and vector b for inspection
    print("Matrix A:\n", A)
    print("Vector b:\n", b)

    # Solve the system
    try:
        Saux = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        print("Error: Singular matrix detected.")
        return None

    # Organize output coefficients
    Coef = np.zeros((n - 1, 3))
    for i in range(n - 1):
        Coef[i, :] = Saux[3 * i:3 * i + 3]

    # Print the tracers for debugging
    print("\nCoeficientes de los trazadores cuadráticos:")
    for i, (a, b, c) in enumerate(Coef):
        print(f"{a:.6f}x^2 + {b:.6f}x + {c:.6f}")

    return Coef


import numpy as np

def trazcub(X, Y):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    n = len(X)
    m = 4 * (n - 1)

    A = np.zeros((m, m))
    b = np.zeros(m)

    # Interpolation conditions (fitting the splines to points)
    row = 0
    for i in range(n - 1):
        A[row, 4 * i:4 * i + 4] = [X[i]**3, X[i]**2, X[i], 1]
        b[row] = Y[i]
        row += 1
        A[row, 4 * i:4 * i + 4] = [X[i + 1]**3, X[i + 1]**2, X[i + 1], 1]
        b[row] = Y[i + 1]
        row += 1

    # Continuity conditions (ensuring derivatives match between segments)
    for i in range(1, n - 1):
        A[row, 4 * (i - 1):4 * (i + 1)] = [
            3 * X[i]**2, 2 * X[i], 1, 0,
            -3 * X[i]**2, -2 * X[i], -1, 0
        ]
        b[row] = 0
        row += 1

    # Smoothness conditions (ensuring second derivatives match between segments)
    for i in range(1, n - 1):
        A[row, 4 * (i - 1):4 * (i + 1)] = [
            6 * X[i], 2, 0, 0,
            -6 * X[i], -2, 0, 0
        ]
        b[row] = 0
        row += 1

    # Natural spline boundary conditions (second derivative is zero at endpoints)
    A[row, 0:2] = [6 * X[0], 2]
    b[row] = 0
    row += 1
    A[row, -4:-2] = [6 * X[-1], 2]
    b[row] = 0

    # Print the matrix A and vector b for inspection
    print("Matrix A:\n", A)
    print("Vector b:\n", b)

    # Solve the system
    try:
        Saux = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        print("Error: Singular matrix detected.")
        return None

    Coef = np.zeros((n - 1, 4))
    for i in range(n - 1):
        Coef[i, :] = Saux[4 * i:4 * i + 4]

    print("\nCoeficientes de los trazadores cúbicos:")
    for i, (a, b, c, d) in enumerate(Coef):
        print(f"{a:.6f}x^3 + {b:.6f}x^2 + {c:.6f}x + {d:.6f}")

    return Coef



A = [[4,-1,0,3], [1,15.5,3,8], [0,-1.3,-4,1.1], [14,5,-2,30]]
b = [1, 1, 1, 1]
x0 = [0, 0, 0, 0]
tol = 1e-7
N_max = 100
w = 1.5
x=[-1,0,3,4]
y=[15.5,3,8,1]
LU_simple(A, b)
print("----------------------------------------------------------------------------------------------------------")
LU_partial(A, b)
print("----------------------------------------------------------------------------------------------------------")
seidel(A, b, x0, tol, N_max)
print("----------------------------------------------------------------------------------------------------------")
SOR(A, b, x0, w, tol, N_max)
print("----------------------------------------------------------------------------------------------------------")
difdivididas(x,y)
print("----------------------------------------------------------------------------------------------------------")
lagrange(x,y)
print("----------------------------------------------------------------------------------------------------------")
trazlin(x,y)
print("----------------------------------------------------------------------------------------------------------")
trazcuad(x,y)
print("----------------------------------------------------------------------------------------------------------")
trazcub(x,y)