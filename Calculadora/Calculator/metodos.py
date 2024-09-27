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

def validate_function(function):
    try:
        function = sp.sympify(function) 
        response = 1
    except sp.SympifyError:
        response = 2
        return response

# Graph function
def graph(function, variable):
    try:
        expr = sp.sympify(function) 
        
    except sp.SympifyError:
        return HttpResponse("The function is not valid.")
    
    var = sp.symbols(variable)
    f = sp.lambdify(var, expr, modules=["numpy"])
    
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
    
# Bisection method function
def bisection(a, b, function, tolerance, variable):
    new_a = float(a)
    new_b = float(b)
    if not root_existence(new_a, new_b, function, variable):
        return False
    
    tolerance = float(tolerance)
    expr = sp.sympify(function) 
    f = sp.lambdify(variable, expr, modules=["numpy"])
    cumple = 0
    iter = 0
    table = []
    error = 0
    print(new_a, new_b, tolerance, f)
    while cumple == 0 and iter < 100:
        c = new_a + ((new_b - new_a)/2)
        fa = f(new_a)
        fb = f(new_b)
        fc = f(c)
        table.append([iter,new_a, c, new_b, fa, fc, error])
        if fa * fc < 0:
            new_b = c
        elif fc * fb < 0:
            new_a = c
        else:
            return None, None, iter, "there is no root in the interval entered for this function"
        error = (new_b - new_a)/2
        if(error <= tolerance):
            cumple  = 1
            table.append([iter, new_a, c, new_b, fa, fc, error])
        else:
            cumple = 0
        iter +=1
    if cumple == 1:
        scientific_notation = "{:.5e}".format(error)
        return c, iter, scientific_notation, table
    else:
        return None, None, iter, "No convergence within the maximum number of iterations"
    
    
    
# Verify the root existence
def root_existence(a, b, fun, var):
    f = symplified_function(fun, var)
    fa = f(a)
    fb = f(b)
    
    if fa*fb < 0:
        return True
    else:
        return False
    

def symplified_function(fun, var):
    expr = sp.sympify(fun) 
    variable = sp.symbols(var)
    function = sp.lambdify(variable, expr, modules=["numpy"])
    return function

# Newton method
def newton_method(x0,tolerance, function, variable):
    x0 = float(x0)
    tolerance = float(tolerance)
    x0_anterior = x0
    var =sp.symbols(variable)
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