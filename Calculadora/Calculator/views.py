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
    image_base64 = graph(function, variable)
    
    try:
        if not bisection(a, b, function, tolerance, variable):
            context = {
                "result": f"There is no roots in this interval [{a}, {b}]",
                "type": 1,
                "buffer": image_base64
            }
            return JsonResponse(context)
        c, iter, error, table = bisection(a, b, function, tolerance, variable)
        
    except Exception as e:  
        return HttpResponse(f"Error in bisection method: {e}")
    context = {
        'buffer': image_base64,
        "result": {
            "root_result" : c,
            "iter": iter,
            "error": error,
            "table": table
        },
        "type": 2
    }
    return JsonResponse(context)

def graph_function(request):
    data = json.loads(request.body)
    function = data["function"]
    variable = data["variable"]

    try:
        image = graph(function, variable)
        return JsonResponse({'image': image})
    except Exception as e:
        return HttpResponse(f"Error showing the graph: {e}")