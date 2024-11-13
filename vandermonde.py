import numpy as np

def vandermonde_matrix(x):
    n = len(x)
    V = np.vander(x)
    print("Vandermonde matrix:")
    for row in V:
        formatted_row = " ".join(f"{elem:.6f}" for elem in row)
        print(formatted_row)
    return V

def polynomial_string(coef, x):
    n = len(coef)
    terms = []
    for i in range(n):
        term = f"{coef[i]:.6f}"
        grado =n - 1 - i
        if grado > 0:
            term += f"x^{grado}"
        if coef[i] > 0 and i != 0:
            terms.append('+' + term)
        else:
            terms.append(term)

    return ''.join(terms)

#Datos
x = np.array([-1, 0, 3, 4])
y = np.array([15.5, 3, 8, 1])

V = vandermonde_matrix(x)

coef = np.linalg.solve(V, y)
print("\nPolynomial coefficients:")

m =""
for i in coef:
    m += f"{i:.6f} "
print(m.strip())

polynomial = polynomial_string(coef, x)
print("\nPolynomial")
print(polynomial)