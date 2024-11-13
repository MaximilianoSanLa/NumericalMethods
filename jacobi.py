
import numpy as np

def jacobi(A,b,x0,tol,n):
    m = ""
    D=np.diag(np.diag(A))
    LU=A-D
    D_inv = np.linalg.inv(D)
    T = np.dot(-D_inv, LU)
    C = np.dot(D_inv, b)
    #spectral radius
    eigenval = np.linalg.eigvals(T)
    spectral_radius =max(abs(eigenval))

    print("\n T:")
    for row in T:
        formatted_row = " ".join(f"{elem:.6f}" for elem in row)
        print(formatted_row)
    print("\n C:")
    for i in C:
        m += f"{i:.6f} "
    print(m.strip())
    print("\n Spectral radius:")
    print(f"{spectral_radius:.6f}")
    print("\n| iter |     E    |")
    x = x0
    for i in range (n):
        x_temp = x
        x= np.dot(D_inv,np.dot(-LU,x))+np.dot(D_inv,b)
        error_absoluto = np.linalg.norm(x - x_temp)
        print(f"| {i+1: <4} | {error_absoluto:.2e} |", end=" ")
        print(" ".join(f"{val: .6f}" for val in x))
        if np.linalg.norm(x-x_temp)<tol:
            return x
    return x


A=np.array([
    [4,-1,0,3],
    [1,15.5,3,8],
    [0,-1.3,-4,1.1],
    [14,5,-2,30]
])
b=([1,1,1,1])
x0 =np.zeros(4)
tol =10**(-7)
n=100
x = jacobi(A,b,x0,tol,n)
