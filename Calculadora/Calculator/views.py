from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
import json

def Calculator(request):
    nombre = metodo.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        "first_name": nombre[0].x
    }
    return HttpResponse(template.render(context, request))

def fun_bisection(request):
    data = json.loads(request.body)
    a = data["a"]
    b = data["b"]
    tolerance = data["tolerance"]
    function = data["function"]
    variable = data["variable"]
    
    
    try:
        new_a, new_b, iter, error = bisection(a, b, function, tolerance, variable)
    except Exception as e:
        return HttpResponse(f"Error in bisection method: {e}")
    image_base64 = graph(function, variable)

    context = {
        'buffer': image_base64,
        "result": {
            "a": new_a,
            "b": new_b,
            "iter": iter,
            "error": error
        }
    }

    return JsonResponse(context)
