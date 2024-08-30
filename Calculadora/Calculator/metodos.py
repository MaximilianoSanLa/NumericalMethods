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
    plt.figure(figsize=(4, 4))
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
    
def bisection(a, b, function, tolerance, variable):
    new_a = float(a)
    new_b = float(b)
    tolerance = float(tolerance)
    f = sp.lambdify(variable, function, modules=["numpy"])
    cumple = 0
    iter = 1
    while cumple == 0 and iter <= 100:
        c = new_a + ((new_b - new_a)/2)
        fa = f(new_a)
        fb = f(new_b)
        fc = f(c)
        
        if fa * fc < 0:
            new_b = c
        else:
            new_a = c
        
        error = (new_b - new_a)/2
        if(error <= tolerance):
            cumple  = 1
        else:
            cumple = 0
        iter +=1
    if cumple == 1:
        scientific_notation = "{:.5e}".format(error)
        return new_a, new_b, iter, scientific_notation
        