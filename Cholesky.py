import numpy as np

def cholesky(A, b):
    n = len(A)
    L = np.zeros((n, n), dtype=complex)  # Matriz L para números reales o complejos

    print("Etapa 0\n")
    print_matrix(A)

    for i in range(n):
        for j in range(i + 1):
            if i == j:  
                L[i, j] = np.sqrt(A[i, i] - sum(L[i, k]**2 for k in range(j)))
            else:  
                L[i, j] = (A[i, j] - sum(L[i, k] * L[j, k] for k in range(j))) / L[j, j]

        # Mostrar matrices L y U después de cada etapa
        print(f"\nEtapa {i + 1}\n")
        print("\nL:")
        print_matrix(L)
        print("\nU:")
        U = L.T.conj()  # La transpuesta conjugada de L
        print_matrix(U)

    # Sustitución progresiva para resolver Ly = b
    y = np.zeros(n, dtype=complex)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, k] * y[k] for k in range(i))) / L[i, i]

    # Sustitución regresiva para resolver Ux = y
    x = np.zeros(n, dtype=complex)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, k] * x[k] for k in range(i + 1, n))) / U[i, i]

    print("\n\nDespués de aplicar sustitución progresiva y regresiva\n")
    print("x:")
    for value in x:
        print(f"{value.real:.6f}")  # Mostrar solo la parte real de la solución

    return x

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value.real:.6f}" if value.imag == 0 else f"{value:.6f}" for value in row))

# Datos de entrada
A = np.array([[4, -1, 0, 3],
              [1, 15.5, 3, 8],
              [0, -1.3, -4, 1.1],
              [14, 5, -2, 30]], dtype=float)
b = np.array([1, 1, 1, 1], dtype=float)

# Resolver usando el método de Cholesky
x = cholesky(A, b)
