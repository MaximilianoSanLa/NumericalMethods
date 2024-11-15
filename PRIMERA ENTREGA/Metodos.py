import numpy as np
import sympy as sp
    
# Function to verify the root existe in some interval
def root_existence(a, b, fun):
    f = symplified_function(fun)
    fa = f(a)
    fb = f(b)
    
    if fa*fb < 0:
        return True
    else:
        return False
    
# incremental search
def search(f, x0, delta, N):
    f = symplified_function(f)
    print("\nIncremental search")
    print("Results\n")
    for i in range(N):
        x1 = x0+delta
        if f(x0)*f(x1) < 0:
            print(f"There is a root of f in [{x0}, {x1}]")
        x0 = x1
    
# Function to symplify a function
def symplified_function(fun):
    expr = sp.sympify(fun) 
    variable = sp.symbols("x")
    function = sp.lambdify(variable, expr, modules=["numpy"])
    return function

# functon for backward sustitution
def sustReg(M):
    n = M.shape[0]
    x = np.zeros(n)

    x[n-1] = M[n-1, n] / M[n-1, n-1]
    for i in range(n-2, -1, -1):
        aux = np.concatenate(([1], x[i+1:n]))
        aux1 = np.concatenate(([M[i, n]], -M[i, i+1:n]))
        x[i] = np.dot(aux, aux1) / M[i, i]
    return x

# Bisection method 
def bisection(a, b, function, tolerance):
    new_a = a
    new_b = b
    tolerance = tolerance
    if not root_existence(new_a, new_b, function):
        print("It does not change signs")
    
    expr = sp.sympify(function) 
    f = sp.lambdify("x", expr, modules=["numpy"])
    cumple = 0
    iteration = 0
    table = []
    error = 0
    
    while cumple == 0 and iteration < 100:
        c = new_a + ((new_b - new_a)/2)
        fa = f(new_a)
        fb = f(new_b)
        fc = f(c)
        
        if iteration == 0:
            error = None
            table.append([iteration,new_a, c, new_b, "{:.5e}".format(fc), error])
        else:
            error = abs(c-c_previus)
            if error <= tolerance:
                cumple = 1
            else: 
                cumple = 0
            table.append([iteration, new_a, c, new_b, "{:.5e}".format(fc), "{:.5e}".format(error)])
        if fa * fc < 0:
            new_b = c
        elif fc * fb < 0:
            new_a = c
        else:
            print( "It does not change signs")
            
        iteration +=1
        c_previus = c 
    if cumple == 1:
        print(f"Bisection \nResults table:\n")
    else:
        print( "No convergence within the maximum number of iterations")
    print("| {:^4} | {:^15} | {:^15} | {:^15} | {:^18} | {:^18} |".format("i", "a", "xm", "b", "f(xm)", "Error absoluto"))
    for row in table:
        print("| {:<4} | {:<15.10f} | {:<15.10f} | {:<15.10f} | {:<18} | {:<18} |".format(
            row[0], row[1], row[2], row[3], row[4], row[5] if row[5] is not None else "0"
        ))
        
# Regla Falsa 
def regla_falsa(function, a, b, tolerance, N):
    f = symplified_function(function)
    if not root_existence(a, b, function):
        print("It does not change signs")
    error = None 
    table = [] 
    cumple = 0
    iteration = 1
    c = (f(b)*a-f(a)*b)/(f(b)-f(a))
    if f(c) == 0:
        print(f"Root: {c}")
    table.append([0, a, c, b, "{:.5e}".format(f(c)), error])
    if f(a)*f(c) < 0:
        new_a = a
        new_b = c
    else:
        new_a = c
        new_b = b
    c_previous = c
    
    while cumple == 0 and iteration < N:
        c = ((f(new_b)*new_a)-(f(new_a)*new_b))/(f(new_b)-f(new_a))
        error = abs(c-c_previous)
        
        if error <= tolerance:
            cumple = 1
        else:
            cumple = 0
        table.append([iteration, new_a, c, new_b, "{:.5e}".format(f(c)), "{:.5e}".format(error)])
        if f(a)*f(c) < 0:
            new_a = new_a
            new_b = c
        else:
            new_a = c
            new_b = new_b
        c_previous = c
        iteration += 1
    if cumple == 1:
        print(f"Regla Falsa \nResults table:\n")
    else:
        print( "No convergence within the maximum number of iterations")
    print("| {:^4} | {:^15} | {:^15} | {:^15} | {:^18} | {:^18} |".format("i", "a", "xm", "b", "f(xm)", "Error absoluto"))
    for row in table:
        print("| {:<4} | {:<15.10f} | {:<15.10f} | {:<15.10f} | {:<18} | {:<18} |".format(
            row[0], row[1], row[2], row[3], row[4], row[5] if row[5] is not None else "0"
        ))
               
#  Punto fijo method
def punto_fijo(function, g_function, x0, tolerance, N):
    f = symplified_function(function)
    g = symplified_function(g_function)
    table = [] 
    iteration = 1
    error = None
    table.append([0, x0, "{:.5e}".format(g(x0)), "{:.5e}".format(f(x0)), error])
    cumple = 0
    x0_anterior = x0
    x0 = g(x0)
    
    while cumple == 0 and iteration < N:
        error = abs(x0-x0_anterior)
        if error < tolerance:
            cumple = 1
        else:
            cumple = 0
        table.append([iteration, x0, "{:.5e}".format(g(x0)), "{:.5e}".format(f(x0)), "{:.5e}".format(error)])
        x0_anterior = x0
        x0 = g(x0)
        iteration += 1
    if cumple == 1:
        print(f"Punto Fijo \nResults table:\n")
    else:
        print( "No convergence within the maximum number of iterations")
    print("| {:^4} | {:^15} | {:^18} | {:^18} | {:^18} |".format("i", "xi", "g(xi)", "f(xi)", "Error absoluto"))
    for row in table:
        print("| {:<4} | {:<15.10f} | {:<18} | {:<18} | {:<18} |".format(
            row[0], row[1], row[2], row[3], row[4] if row[4] is not None else "0"
        ))
    
# Newton method
def newton(x0,tolerance, function, N):
    x0 = float(x0)
    tolerance = float(tolerance)
    x0_anterior = x0
    expr = sp.sympify(function) 
    f = symplified_function(function)
    df_expr = sp.diff(expr) 
    df = sp.lambdify("x", df_expr, modules=["numpy"])
    iteration = 0
    error = 0
    table = []
    cumple = 0

    while cumple == 0 and iteration < N:
        df_x0 = df(x0)
        f_x0 = f(x0)
        if abs(df_x0) == 0:
            return None

        if iteration == 0:
            error = None
            table.append([iteration, x0, "{:.5e}".format(f_x0), "{:.5e}".format(df_x0), error])
        else:
            error = abs(x0 - x0_anterior)
            if error <= tolerance:
                cumple = 1
            else: 
                cumple = 0
            table.append([iteration, x0, "{:.5e}".format(f_x0), "{:.5e}".format(df_x0), "{:.5e}".format(error)])
        x0_anterior = x0
        x0 = x0 - (f_x0 / df_x0)
        iteration +=1
    
    if cumple == 1:
        print(f"Newton \nResults table:\n")
    else:
        print( "No convergence within the maximum number of iterations")
    print("| {:^4} | {:^15} | {:^18} | {:^18} | {:^18} |".format("i", "xi", "f(xi)", "f'(xi)", "Error absoluto"))
    for row in table:
        print("| {:<4} | {:<15.10f} | {:<18} | {:<18} | {:<18} |".format(
            row[0], row[1], row[2], row[3], row[4] if row[4] is not None else "0"
        ))
        
# Secant method
def secant(x0, x1, tolerance, N, function):
    f = symplified_function(function)
    iteration = 2
    cumple = 0
    table = []
    error = None
    table.append([0, x0, "{:.5e}".format(f(x0)), error])
    table.append([1, x1, "{:.5e}".format(f(x1)), error])
    x1 = x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)))

    while cumple == 0 and iteration < N:
        denominador = f(x1) - f(x0)
        if abs(denominador) == 0:
            print(f"Error. Dividing by 0")

        error = abs(x1 - x0)
        if error <= tolerance:
            cumple = 1
        else: 
            cumple = 0
        error = abs(x1 - x0)
        table.append([iteration, x1, "{:.5e}".format(f(x1)), "{:.5e}".format(error)])
        x2 = x1-((f(x1)*(x1-x0))/denominador)
        x0 = x1
        x1 = x2
        iteration += 1
    if cumple == 1:
        print(f"Secant \nResults table:\n")
    else:
        print( "No convergence within the maximum number of iterations")
    print("| {:^4} | {:^15} | {:^18} | {:^18} |".format("i", "xi", "f(xi)", "Error absoluto"))
    for row in table:
        print("| {:<4} | {:<15.10f} | {:<18} | {:<18} |".format(
            row[0], row[1], row[2], row[3] if row[3] is not None else "0"
        ))
    
# Multiple roots method
def multiple_roots(function, d_function, dd_function, x0, tolerance, N):
    xi = x0
    history = []
    cumple = 0
    h = symplified_function(function)
    dh = symplified_function(d_function)
    ddh = symplified_function(dd_function)

    for i in range(N):
        
        hi = h(xi)
        
        dhi = dh(xi)
        
        ddhi = ddh(xi)
        
        # function for multiple roots
        xi_new = xi - ((hi * dhi) / (dhi**2 - hi * ddhi))
        
        error = abs(xi_new - xi)
        history.append((i, xi, "{:.5e}".format(hi), "{:.5e}".format(error)))
        
        if error < tolerance:
            cumple = 1
            break
        
        xi = xi_new
        
    if cumple == 1:
        print(f"Multiple roots \nResults table:\n")
    else:
        print( "No convergence within the maximum number of iterations")
    print("| {:^4} | {:^15} | {:^18} | {:^18} |".format("i", "xi", "h(xi)", "Error absoluto"))
    for row in history:
        print("| {:<4} | {:<15.10f} | {:<18} | {:<18} |".format(
            row[0], row[1], row[2], row[3]
        ))

# Gaussian simple elimination method
def gausspl(A, b):
    n = A.shape[0]
    M = np.hstack((A, b.reshape(-1, 1)))
    print("Gaussian simple elimination\n")
    print("Results:\n")
    # if(M[0][0]==0):
    #     return "Matriz en 0"
    print(f"Stage {0}\n")
    for row in M:
        print(" ".join("{: .6f}".format(element) for element in row))
    print("\n")
    for i in range(n-1):
        print(f"Stage {i+1}\n")
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i] / M[i, i]) * M[i, i:n+1]
        for row in M:
            print(" ".join("{: .6f}".format(element) for element in row))
        print("\n")
    print("after applying backward sustitution\n")
    print("x:\n")
    x = sustReg(M)
    for row in x:
        print(row)
    
# Gaussian elimination with partial pivoting
def gausspar(A, b):
    n = A.shape[0]
    M = np.hstack((A, b.reshape(-1, 1)))
    print("Gaussian simple elimination\n")
    print("Results:\n")
    M = M.astype(np.float64)
    print(f"Stage {0}\n")
    for row in M:
        print(" ".join("{: .6f}".format(element) for element in row))
    print("\n")
    for i in range(n-1):
        print(f"Stage {i+1}\n")
        abs_col = np.abs(M[i+1:n, i])
        max_val = np.max(abs_col)
        max_row = np.argmax(abs_col) + i + 1

        if max_val > np.abs(M[i, i]):
            M[[i, max_row], i:n+1] = M[[max_row, i], i:n+1]

        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] -= (M[j, i] / M[i, i]) * M[i, i:n+1]
        for row in M:
            print(" ".join("{: .6f}".format(element) for element in row))
        print("\n")
        
    print("after applying backward sustitution\n")
    print("x:\n")
    x = sustReg(M)
    for row in x:
        print(row)
        
# Gaussian elimination with total pivoting
def gausstot(A, b):
    # Initialization
    n = A.shape[0]
    M = np.hstack((A, b.reshape(-1, 1)))
    cambi = []
    M = M.astype(np.float64)
    print("Gaussian simple elimination\n")
    print("Results:\n")
    print(f"Stage {0}\n")
    for row in M:
        print(" ".join("{: .6f}".format(element) for element in row))
    print("\n")
    for i in range(n-1):
        print(f"Stage {i+1}\n")
        submatrix = np.abs(M[i:n, i:n])
        a, b = np.unravel_index(np.argmax(submatrix), submatrix.shape)
        a += i
        b += i

        # Column swapping
        if b != i:
            cambi.append((i, b))
            M[:, [i, b]] = M[:, [b, i]]

        # Row swapping
        if a != i:
            M[[i, a], i:n+1] = M[[a, i], i:n+1]

        # Gaussian elimination
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] -= (M[j, i] / M[i, i]) * M[i, i:n+1]
        for row in M:
            print(" ".join("{: .6f}".format(element) for element in row))
        print("\n")

    # Back substitution
    x = sustReg(M)

    # Reorder the solution vector based on column swaps
    for i in range(len(cambi)-1, -1, -1):
        x[cambi[i][0]], x[cambi[i][1]] = x[cambi[i][1]], x[cambi[i][0]]

    print("after applying backward sustitution\n")
    print("x:\n") 
    for row in x:
        print(row)

search("ln((sin(x))^2+1)-1/2", -3, 0.5, 100)
print("----------------------------------------------------------------------------------------------------------")
bisection(0, 1, "ln((sin(x))^2+1)-1/2", 1e-7)
print("----------------------------------------------------------------------------------------------------------")
regla_falsa("ln((sin(x))^2+1)-1/2", 0, 1, 1e-7, 100)
print("----------------------------------------------------------------------------------------------------------")
punto_fijo("ln((sin(x))^2+1)-(1/2)-x", "ln((sin(x))^2+1)-1/2", -0.5, 1e-7, 100)
print("----------------------------------------------------------------------------------------------------------")
newton(0.5, 1e-7, "ln((sin(x))^2+1)-1/2", 100)
print("----------------------------------------------------------------------------------------------------------")
secant(0.5, 1, 1e-7, 100, "ln((sin(x))^2+1)-1/2")
print("----------------------------------------------------------------------------------------------------------")
multiple_roots("exp(x)-x-1", "exp(x)-1", "exp(x)", 1, 1e-7, 100)
print("----------------------------------------------------------------------------------------------------------")

A=np.array([[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]])
b=np.array([[1],[1],[1],[1]])
gausspl(A, b)
print("----------------------------------------------------------------------------------------------------------")
gausspar(A, b)
print("----------------------------------------------------------------------------------------------------------")
gausstot(A, b)
