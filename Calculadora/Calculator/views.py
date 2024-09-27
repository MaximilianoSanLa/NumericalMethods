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

def incremental_search_method(request):
    data = json.loads(request.body)
    f = data["function"]
    x0 = data["x0"]
    delta = data["delta"]
    N = data["N"]
    image_base64 = graph(f)
    
    try:
        table = incremental_search(f, x0, delta, N)
        if len(table) == 0:
            return JsonResponse({"result": "empty table", "buffer": image_base64})
        return JsonResponse({"result": table, "buffer": image_base64})
    except Exception as e:  
        return HttpResponse(f"Error in incremental search method: {e}")
        

# Bisection method
def fun_bisection(request):
    data = json.loads(request.body)
    a = data["a"]
    b = data["b"]
    tolerance = data["tolerance"]
    function = data["function"]
    N = data["N"]
    image_base64 = graph(function)
    try:
        if bisection(a, b, function, tolerance, N) == "no root in the interval":
            context = {
                "result": f"There is no roots in this interval [{a}, {b}]",
                "type": "no root in the interval",
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif bisection(a, b, function, tolerance, N) == "invalid_function":
            context = {
                "result": "invalid function",
                "type": "invalid function",
                "buffer": image_base64
                
            }
            return JsonResponse(context)
        elif bisection(a, b, function, tolerance, N)[0] == "no convergence":
            context = {
                "result": bisection(a, b, function, tolerance, N)[1],
                "type": "no convergence",
                "buffer": image_base64
                
            }
            return JsonResponse(context)
            
        c, iter, error, table = bisection(a, b, function, tolerance, N)
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
        "type" : "succes"
    }
    return JsonResponse(context)

# Regla falsa method
def regla_falsa_method(request):
    data = json.loads(request.body)
    function = data["function"]
    a = data["a"]
    b = data["b"]
    tolerance = data["tolerance"]
    N = data["N"]
    image_base64 = graph(function)
    
    try:
        if regla_falsa(function, a, b, tolerance, N) == "no root in the interval":
            context = {
                "result": f"There is no roots in this interval [{a}, {b}]",
                "type": "no root in the interval",
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif regla_falsa(function, a, b, tolerance, N) == "invalid_function":
            context = {
                "result": "invalid function",
                "type": "invalid function",
                "buffer": image_base64
                
            }
            return JsonResponse(context)
        elif regla_falsa(function, a, b, tolerance, N)[0] == "no convergence":
            context = {
                "result": regla_falsa(function, a, b, tolerance, N)[1],
                "type": "no convergence",
                "buffer": image_base64
                
            }
            return JsonResponse(context)
            
        c, iter, error, table = regla_falsa(function, a, b, tolerance, N)
    except Exception as e:  
        return HttpResponse(f"Error in regla falsa method: {e}")
    context = {
        'buffer': image_base64,
        "result": {
            "root_result" : c,
            "iter": iter,
            "error": error,
            "table": table
        },
        "type" : "succes"
    }
    return JsonResponse(context)

# graph function
def graph_function(request):
    data = json.loads(request.body)
    function = data["function"]

    try:
        image = graph(function)
        return JsonResponse({'image': image})
    except Exception as e:
        return HttpResponse(f"Error showing the graph: {e}")
    
# Newton method
def newton(request):
    data = json.loads(request.body)
    x0 = data["x0"]
    tolerance = data["tolerance"]
    function = data["function"]
    image_base64 = graph(function)
    
    try:
        if newton_method(x0, tolerance, function) is None:
            context = {
                "result": f"Dividing by 0",
                "type": 1,
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif newton_method(x0, tolerance, function) == "run out if iterations":
            context = {
                "result": "Run out of iterations",
                "type": 3,
                "buffer": image_base64
            }
            return JsonResponse(context)
        iterations, xi, error, table = newton_method(x0, tolerance, function)
        print(iterations, xi, error, table)
    except Exception as e:  
        return HttpResponse(f"Error in newton method: {e}")
    context = {
        'buffer': image_base64,
        "result": {
            "root_result" : xi,
            "iter": iterations,
            "error": error,
            "table": table
        },
        "type": 2
    }
    return JsonResponse(context)
