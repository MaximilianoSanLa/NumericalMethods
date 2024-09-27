from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import metodo
from .metodos import *
import math
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
        return "no convergence", table
    
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
        return "no convergence", table

# Newton method
def newton_method(x0,tolerance, function):
    x0 = float(x0)
    tolerance = float(tolerance)
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

    while cumple == 0 and iteration < 100:
        print(x0, x0_anterior, iteration, error)
        df_x0 = df(x0)
        f_x0 = f(x0)
        if abs(df_x0) == 0:
            return None

        if iteration == 0:
            error = None
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
    return "run out of iterations"