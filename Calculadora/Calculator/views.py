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

def Calculator(request):
    nombre = metodo.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        "first_name": nombre[0].x
    }
    return HttpResponse(template.render(context, request))

def fun_bisection(request):
    template = loader.get_template("grafica.html")
    function = request.GET.get('function', '2*x + 1') 
    variable = request.GET.get("variable")
    a = request.GET.get("a")
    b = request.GET.get("b")
    tolerance = request.GET.get("tolerance")
    
    try:
        new_a, new_b, iter, error = bisection(a, b, function, tolerance, variable)
    except Exception as e:
        return HttpResponse(f"Error in bisection method: {e}")
    image_base64 = graph(function, variable)

    context = {
        'buffer': image_base64,
        "a": new_a,
        "b": new_b,
        "iter": iter,
        "error": error
    }

    return HttpResponse(template.render(context, request))
