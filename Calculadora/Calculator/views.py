from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import metodo
import math
import io
import matplotlib.pyplot as plt
import numpy as np
import base64
import sympy as sp

def Calculator(request):
    nombre = metodo.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        "first_name": nombre[0].x
    }
    return HttpResponse(template.render(context, request))


def funcion(request):
    template = loader.get_template("grafica.html")
    ecuacion = request.GET.get('function', '2*x + 1') 
    variable = request.GET.get("variable")
    
    try:
        expr = sp.sympify(ecuacion) 
    except sp.SympifyError:
        return HttpResponse("The function is not valid.")
    
    if variable == "x":
        x = sp.symbols("x")
        var = x
        plt.xlabel("x")
        plt.ylabel("y")
    else:
        y = sp.symbols("y")
        var = y
        plt.xlabel("y")
        plt.ylabel("x")
    f = sp.lambdify(var, expr, modules=["numpy"])
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)
    plt.figure(figsize=(6, 4))
    plt.plot(x_vals, y_vals, label=f"{var} = {ecuacion}")
    
    plt.title(f"Graph of the function {var} = {ecuacion}")
    plt.legend()
    plt.grid(True)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    
    plt.close()
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    context = {'buffer': image_base64}

    return HttpResponse(template.render(context, request))
