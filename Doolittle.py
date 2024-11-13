import numpy as np

def doolittle(A, b):
    n = len(A)
    L = np.eye(n)  # Matriz identidad para L
    U = np.zeros((n, n))
    
    print("Etapa 0\n")
    print_matrix(A)
    
    for j in range(n):
        for i in range(j, n):  # Calcular elementos de U
            U[j, i] = A[j, i] - sum(L[j, k] * U[k, i] for k in range(j))
        for i in range(j + 1, n):  # Calcular elementos de L
            L[i, j] = (A[i, j] - sum(L[i, k] * U[k, j] for k in range(j))) / U[j, j]
        
        # Mostrar matrices en cada etapa
        print(f"\nEtapa {j + 1}\n")
        print("\nL:")
        print_matrix(L)
        print("\nU:")
        print_matrix(U)

    # Sustitución progresiva para resolver Ly = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, k] * y[k] for k in range(i))

    # Sustitución regresiva para resolver Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, k] * x[k] for k in range(i + 1, n))) / U[i, i]

    print("\n\nDespués de aplicar sustitución progresiva y regresiva\n")
    print("x:")
    for value in x:
        print(f"{value:.6f}")

    return x

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:10.6f}" for value in row))

# Datos de entrada
A = np.array([[4, -1, 0, 3],
              [1, 15.5, 3, 8],
              [0, -1.3, -4, 1.1],
              [14, 5, -2, 30]], dtype=float)
b = np.array([1, 1, 1, 1], dtype=float)

# Resolver usando el método de Doolittle
x = doolittle(A, b)
