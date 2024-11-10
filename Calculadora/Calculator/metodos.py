from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import metodo
from .metodos import *
import io
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import numpy as np
import base64
import sympy as sp

# valite function
def validate_function(function):
    try:
        function = sp.sympify(function) 
        return True
    except sp.SympifyError:
        return False

# Function to symplify an algebraic expression    
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

# Function to verify the root existence in a given interval
def root_existence(a, b, fun):
    f = symplified_function(fun)
    fa = f(a)
    fb = f(b)
    
    if fa*fb < 0:
        return True
    else:
        return False

# Function to graph a algebraic function
def graph(function):
    if not validate_function(function):
        return "invalid function"
    f = symplified_function(function)
    
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)
    
    plt.ioff()
    plt.figure(figsize=(5, 5))
    plt.plot(x_vals, y_vals, label=f"y = {function}", color='blue')
    plt.axhline(0, color='black', linewidth=1) 
    plt.axvline(0, color='black', linewidth=1)  
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.title(f"Graph of the function {function}")
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['left'].set_position('zero')
    plt.gca().spines['bottom'].set_position('zero')
    plt.gca().xaxis.set_ticks_position('both')
    plt.gca().yaxis.set_ticks_position('both')
    plt.legend()
    
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()
    
    image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return image

# Incremental search function
def incremental_search(f, x0, delta, N):
    if not validate_function(f):
        return "invalid function"
    f = symplified_function(f)
    table = []
    for i in range(N):
        
        x1 = x0+delta
        if f(x0)*f(x1) < 0:
            table.append(f"There is a root of f in {x0}, {x1}")
        x0 = x1
    return table
    
# Bisection method function
def bisection(a, b, function, tolerance, N):
    if not validate_function(function):
        return "invalid_function"
    new_a = a
    new_b = b
    N = int(N)
    if not root_existence(new_a, new_b, function):
        return "no root in the interval"
    expr = sp.sympify(function) 
    f = sp.lambdify("x", expr, modules=["numpy"])
    cumple = 0
    iteration = 0
    table = []
    error = 0
    
    while cumple == 0 and iteration < N:
        c = new_a + ((new_b - new_a)/2)
        fa = f(new_a)
        fb = f(new_b)
        fc = f(c)
        
        if iteration == 0:
            error = 0
            table.append([iteration,new_a, c, new_b, "{:.5e}".format(fa), "{:.5e}".format(fc), error])
        else:
            error = abs(c-c_previous)
            if error <= tolerance:
                cumple = 1
            else: 
                cumple = 0
            table.append([iteration, new_a, c, new_b, "{:.5e}".format(fa), "{:.5e}".format(fc), "{:.5e}".format(error)])
        if fa * fc < 0:
            new_b = c
        else:
            new_a = c
            
        iteration +=1
        c_previous = c 
    if cumple == 1:
        scientific_notation = "{:.5e}".format(error)
        return c, iteration, scientific_notation, table
    else:
        return "ran out of iterations ", table
    
# Regla Falsa 
def regla_falsa(function, a, b, tolerance, N):
    if not validate_function(function):
        return "invalid_function"
    f = symplified_function(function)
    if not root_existence(a, b, function):
        return "no root in the interval"
    error = 0
    table = [] 
    cumple = 0
    iteration = 1
    c = (f(b)*a-f(a)*b)/(f(b)-f(a))
    table.append([0, a, c, b, "{:.5e}".format(f(c)), error])
    if f(c) == 0:
        cumple = 1
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
        scientific_notation = "{:.5e}".format(error)
        return c, iteration, scientific_notation, table
    else:
        return "ran out of iterations", table

#  Punto fijo method
def punto_fijo(function, g_function, x0, tolerance, N):
    if not validate_function(function):
        return "invalid function"
    elif not validate_function(g_function):
        return "invalid function"
    f = symplified_function(function)
    g = symplified_function(g_function)
    table = [] 
    iteration = 1
    error = 0
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
        return iteration, x0, g(x0), f(x0), error, table
    else:
        return "ran out of iterations", table
    
# Newton method
def newton_method(x0,tolerance, function, N):
    if not validate_function(function):
        return "invalid function"
    x0_anterior = x0
    var =sp.symbols("x")
    expr = sp.sympify(function)  
    f = sp.lambdify(var, expr, modules=["numpy"])
    df_expr = sp.diff(expr, var) 
    df = sp.lambdify(var, df_expr, modules=["numpy"])
    iteration = 0
    error = 0
    table = []
    cumple = 0

    while cumple == 0 and iteration < N:
        print(x0, x0_anterior, iteration, error)
        df_x0 = df(x0)
        f_x0 = f(x0)
        if abs(df_x0) == 0:
            return None

        if iteration == 0:
            error = 0
            table.append([iteration, x0, f_x0, df_x0, error])
        else:
            error = abs(x0 - x0_anterior)
            if error <= tolerance:
                cumple = 1
            else: 
                cumple = 0
            error_cientific = "{:.5e}".format(error)
            table.append([iteration, x0, f_x0, df_x0, error_cientific])
        x0_anterior = x0
        x0 = x0 - (f_x0 / df_x0)
        iteration +=1
    
    if cumple == 1:
        return iteration, x0_anterior, error, table
    return "ran out of iterations", table

# Secant method
def secant(x0, x1, tolerance, N, function):
    if not validate_function(function):
        return "invalid function"
    f = symplified_function(function)
    iteration = 2
    cumple = 0
    table = []
    error = 0
    table.append([0, x0, "{:.5e}".format(f(x0)), error])
    table.append([1, x1, "{:.5e}".format(f(x1)), error])
    x1 = x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)))

    while cumple == 0 and iteration < N:
        denominador = f(x1) - f(x0)
        if abs(denominador) == 0:
            return "dividing by 0"

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
        return iteration, x1, f(x1), error, table
    else:
        return "ran out of iterations", table

# Multiple roots method
def multiple_roots(function, x0, tolerance, N):
    if not validate_function(function):
        return "invalid function"
    xi = x0
    history = []
    cumple = 0
    expr = sp.sympify(function)
    h = symplified_function(function)
    dh_expr = sp.diff(expr, "x") 
    dh = symplified_function(dh_expr)
    ddh_expr = sp.diff(dh_expr, "x") 
    ddh = symplified_function(ddh_expr)

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
        return i, xi, hi, error, history
    return "ran out of iterations", history

# Gaussian simple elimination method
def gausspl(A, b):
    A = np.array(A)  
    b = np.array(b)
    n = A.shape[0]
    M = np.hstack((A, b.reshape(-1, 1)))
    # if(M[0][0]==0):
    #     return "Matriz en 0"
    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i] / M[i, i]) * M[i, i:n+1]
    return sustReg(M)

# Gaussian elimination with partial pivoting
def gausspar(A, b):
    A = np.array(A)  
    b = np.array(b)
    n = A.shape[0]
    M = np.hstack((A, b.reshape(-1, 1)))
    M = M.astype(np.float64)
    for i in range(n-1):
        abs_col = np.abs(M[i+1:n, i])
        max_val = np.max(abs_col)
        max_row = np.argmax(abs_col) + i + 1

        if max_val > np.abs(M[i, i]):
            M[[i, max_row], i:n+1] = M[[max_row, i], i:n+1]

        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] -= (M[j, i] / M[i, i]) * M[i, i:n+1]
    return sustReg(M)

# Gaussian elimination with total pivoting
def gausstot(A, b):
    A = np.array(A)  
    b = np.array(b)
    # Initialization
    n = A.shape[0]
    M = np.hstack((A, b.reshape(-1, 1)))
    cambi = []
    M = M.astype(np.float64)
    for i in range(n-1):
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
    return sustReg(M)