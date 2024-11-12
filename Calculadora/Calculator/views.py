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
    
    try:
        if graph(f) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        image_base64 = graph(f)
        table = incremental_search(f, x0, delta, N)
        if len(table) == 0:
            return JsonResponse({"result": "empty table", "buffer": image_base64, "type": 1})
        elif incremental_search(f, x0, delta, N) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        return JsonResponse({"result": table, "buffer": image_base64, "type": "succes"})
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
    
    try:
        if graph(function) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        image_base64 = graph(function)
        if bisection(a, b, function, tolerance, N) == "no root in the interval":
            context = {
                "result": "no root in the interval",
                "type": 1,
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif bisection(a, b, function, tolerance, N) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2,
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif bisection(a, b, function, tolerance, N)[0] == "ran out of iterations":
            context = {
                "result": "ran out of iterations",
                "type": 3,
                "table": bisection(a, b, function, tolerance, N)[1],
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
    
    try:
        if graph(function) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        image_base64 = graph(function)
        if regla_falsa(function, a, b, tolerance, N) == "no root in the interval":
            context = {
                "result": "no root in the interval",
                "type": 1,
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif regla_falsa(function, a, b, tolerance, N) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2,
                "buffer": image_base64
                
            }
            return JsonResponse(context)
        elif regla_falsa(function, a, b, tolerance, N)[0] == "ran out of iterations":
            context = {
                "result": "ran out of iterations",
                "type": 3,
                "buffer": image_base64,
                "table": regla_falsa(function, a, b, tolerance, N)[1]
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
        if graph(function) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        image = graph(function)
        return JsonResponse({'image': image})
    except Exception as e:
        return HttpResponse(f"Error showing the graph: {e}")
    
# Punto fijo method
def punto_fijo_method(request):
    data = json.loads(request.body)
    f = data["f"]
    g = data["g"]
    x0 = data["x0"]
    tolerance = data["tolerance"]
    N = data["N"]

    try:
        if graph(f) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 1
            }
            return JsonResponse(context)
        image_base64 = graph(f)
        if graph(g) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 1
            }
            return JsonResponse(context)
        if punto_fijo(f, g, x0, tolerance, N) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 1,
            }
            return JsonResponse(context)
        elif punto_fijo(f, g, x0, tolerance, N)[0] == "ran out of iterations":
            context = {
                "result": "ran out of iterations",
                "type": 2,
                "buffer": image_base64,
                "table": punto_fijo(f, g, x0, tolerance, N)[1]
            }
            return JsonResponse(context)
        iteration, xi, gxi, fxi, error, table  = punto_fijo(f, g, x0, tolerance, N)
    except Exception as e:  
        return HttpResponse(f"Error in punto fijo method: {e}")
    context = {
        'buffer': image_base64,
        "result": {
            "iterations": iteration,
            "xi": xi,
            "gxi": gxi,
            "fxi": fxi,
            "error": error,
            "table": table
        },
        "type": "succes"
    }
    return JsonResponse(context)
    
# Newton method
def newton_method(request):
    data = json.loads(request.body)
    x0 = data["x0"]
    tolerance = data["tolerance"]
    function = data["function"]
    N = data["N"]
    
    try:
        if graph(function) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        image_base64 = graph(function)
        if newton_method(x0, tolerance, function, N) is None:
            context = {
                "result": "Dividing by 0",
                "type": 1,
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif newton_method(x0, tolerance, function, N)[0] == "ran out if iterations":
            context = {
                "result": "Ran out of iterations",
                "type": 2,
                "buffer": image_base64,
                "table": newton_method(x0, tolerance, function, N)[1]
            }
            return JsonResponse(context)
        elif newton_method(x0, tolerance, function, N) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 3,
                "buffer": image_base64
            }
            return JsonResponse(context)
        iterations, xi, error, table = newton_method(x0, tolerance, function, N)
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
        "type": "succes"
    }
    return JsonResponse(context)

# Secant method
def secant_method(request):
    data = json.loads(request.body)
    function = data["function"]
    x0 = data["x0"]
    x1 = data["x1"]
    tolerance = data["tolerance"]
    N = data["N"]
    
    try:
        if graph(function) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        image_base64 = graph(function)
        if secant(x0, x1, tolerance, N, function) == "dividing by 0":
            context = {
                "result": "Dividing by 0",
                "type": 1,
                "buffer": image_base64
            }
            return JsonResponse(context)
        elif secant(x0, x1, tolerance, N, function)[0] == "ran out of iterations":
            context = {
                "result": "ran out of iterations",
                "type": 2,
                "buffer": image_base64,
                "table": secant(x0, x1, tolerance, N, function)[1]
            }
            return JsonResponse(context)
        elif secant(x0, x1, tolerance, N, function) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 3,
                "buffer": image_base64
            }
            return JsonResponse(context)
        iteration, xi, fxi, error, table  = secant(x0, x1, tolerance, N, function)
    except Exception as e:  
        return HttpResponse(f"Error in secant method: {e}")
    context = {
        'buffer': image_base64,
        "result": {
            "iterations": iteration,
            "xi": xi,
            "fxi": fxi,
            "error": error,
            "table": table
        },
        "type": "succes"
    }
    return JsonResponse(context)

# Multiple roots method
def multiple_roots_method(request):
    data = json.loads(request.body)
    function = data["function"]
    x0 = data["x0"]
    tolerance = data["tolerance"]
    N = data["N"]
    
    try:
        if graph(function) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2
            }
            return JsonResponse(context)
        image_base64 = graph(function)
        if multiple_roots(function, x0, tolerance, N)[0] == "ran out of iterations":
            context = {
                "result": "ran out of iterations",
                "type": 1,
                "buffer": image_base64,
                "table": multiple_roots(function, x0, tolerance, N)[1]
            }
            return JsonResponse(context)
        elif multiple_roots(function, x0, tolerance, N) == "invalid function":
            context = {
                "result": "invalid function",
                "type": 2,
                "buffer": image_base64
            }
            return JsonResponse(context)
        iteration, xi, hi, error, table = multiple_roots(function, x0, tolerance, N)
    except Exception as e:  
        return HttpResponse(f"Error in multiple roots method: {e}")
    context = {
        'buffer': image_base64,
        "result": {
            "iteration" : iteration,
            "xi": xi,
            "hi": hi,
            "error": error,
            "table": table
        },
        "type": "succes"
    }
    return JsonResponse(context)

# Gaussian simple elimination method
def gausspl_method(request):
    data = json.loads(request.body)
    A = data["A"]
    b = data["b"]
    
    try:
        x = gausspl(A, b)
        print(x)
    except Exception as e:  
        return HttpResponse(f"Error in Gaussian simple elimination method: {e}")
    return JsonResponse({"result": x.tolist()})

# Gaussian eliminition with partial pivoting method
def gausspar_method(request):
    data = json.loads(request.body)
    A = data["A"]
    b = data["b"]
    
    try:
        x = gausspar(A, b)
    except Exception as e:  
        return HttpResponse(f"Error in Gaussian elimination with partial pivoting method: {e}")
    return JsonResponse({"result": x.tolist()})

# Gaussian eliminition with total pivoting method
def gausstot_method(request):
    data = json.loads(request.body)
    A = data["A"]
    b = data["b"]
    
    try:
        x = gausstot(A, b)
    except Exception as e:  
        return HttpResponse(f"Error in Gaussian elimination with total pivoting method: {e}")
    return JsonResponse({"result": x.tolist()})
