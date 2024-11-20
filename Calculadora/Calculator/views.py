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
import sys
import ast
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
    A = np.array(ast.literal_eval(data["A"]), dtype=float)
    b = np.array(ast.literal_eval(data["b"]), dtype=float)
    print(A)
    print(b)
    
    try:
        x = gausspl(A, b)
        print(x)
    except Exception as e:  
        return HttpResponse(f"Error in Gaussian simple elimination method: {e}")
    return JsonResponse({"result": x.tolist()})

# Gaussian eliminition with partial pivoting method
def gausspar_method(request):
    data = json.loads(request.body)
    A = np.array(ast.literal_eval(data["A"]), dtype=float)
    b = np.array(ast.literal_eval(data["b"]), dtype=float)
    print(A)
    print(b)
    try:
        x = gausspar(A, b)
    except Exception as e:  
        return HttpResponse(f"Error in Gaussian elimination with partial pivoting method: {e}")
    return JsonResponse({"result": x.tolist()})

# Gaussian eliminition with total pivoting method
def gausstot_method(request):
    data = json.loads(request.body)
    A = np.array(ast.literal_eval(data["A"]), dtype=float)
    b = np.array(ast.literal_eval(data["b"]), dtype=float)
    
    try:
        x = gausstot(A, b)
    except Exception as e:  
        return HttpResponse(f"Error in Gaussian elimination with total pivoting method: {e}")
    return JsonResponse({"result": x.tolist()})

def sustprgr(L_b):
    n = L_b.shape[0]
    L = L_b[:, :-1]
    b = L_b[:, -1]
    z = np.zeros(n)
    for i in range(n):
        z[i] = (b[i] - np.dot(L[i, :i], z[:i])) / L[i, i]
    return z

def sustregr(U_z):
    n = U_z.shape[0]
    U = U_z[:, :-1]
    z = U_z[:, -1]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (z[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

def LU_simple(request):
    data = json.loads(request.body)
    A = np.array(ast.literal_eval(data["A"]), dtype=float)
    b = np.array(ast.literal_eval(data["b"]), dtype=float)
    try:

        n = A.shape[0]
        L = np.eye(n)
        U = np.zeros((n, n))
        M = A.copy()

        # Gaussian elimination steps
        for i in range(n-1):
            for j in range(i+1, n):
                if M[j, i] != 0:
                    L[j, i] = M[j, i] / M[i, i]
                    M[j, i:n] = M[j, i:n] - (M[j, i] / M[i, i]) * M[i, i:n]
            U[i, i:n] = M[i, i:n]
            U[i+1, i+1:n] = M[i+1, i+1:n]

        U[n-1, n-1] = M[n-1, n-1]
        z = sustprgr(np.column_stack((L, b)))
        x = sustregr(np.column_stack((U, z)))

        return JsonResponse({
            "L": L.tolist(),
            "U": U.tolist(),
            "x": x.tolist(),
            "message": "LU decomposition completed successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
def LU_partial(request):
    data = json.loads(request.body)
    A = np.array(ast.literal_eval(data["A"]), dtype=float)
    b = np.array(ast.literal_eval(data["b"]), dtype=float)
    try:
        n = A.shape[0]
        L = np.eye(n)
        U = np.zeros((n, n))
        P = np.eye(n)
        M = A.copy()

        for i in range(n-1):
            max_index = np.argmax(abs(M[i+1:n, i])) + i + 1
            if abs(M[max_index, i]) > abs(M[i, i]):
                M[[i, max_index], i:n] = M[[max_index, i], i:n]
                P[[i, max_index], :] = P[[max_index, i], :]
                
            for j in range(i+1, n):
                if M[j, i] != 0:
                    L[j, i] = M[j, i] / M[i, i]
                    M[j, i:n] -= (M[j, i] / M[i, i]) * M[i, i:n]
            U[i, i:n] = M[i, i:n]
            U[i+1, i+1:n] = M[i+1, i+1:n]

        U[n-1, n-1] = M[n-1, n-1]
        z = sustprgr(np.column_stack((L, np.dot(P, b))))
        x = sustregr(np.column_stack((U, z)))

        return JsonResponse({
            "L": L.tolist(),
            "U": U.tolist(),
            "P": P.tolist(),
            "x": x.tolist(),
            "message": "LU with partial pivoting completed successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
def crout(request):
    data = json.loads(request.body)
    A = np.array(ast.literal_eval(data["A"]), dtype=float)
    b = np.array(ast.literal_eval(data["b"]), dtype=float)
    n = len(A)
    L = np.zeros((n, n))
    U = np.eye(n)  # Matriz identidad para U
    
    
    for j in range(n):
        for i in range(j, n):  # Calcular elementos de L
            L[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(j))
        for i in range(j + 1, n):  # Calcular elementos de U
            U[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(j))) / L[j, j]

    # Sustitución progresiva para resolver Ly = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, k] * y[k] for k in range(i))) / L[i, i]

    # Sustitución regresiva para resolver Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(U[i, k] * x[k] for k in range(i + 1, n))
    
    return JsonResponse({
            "L": L.tolist(),
            "U": U.tolist(),
            "x": x.tolist()
        })

def doolittle(request):
    data = json.loads(request.body)
    A = np.array(data["A"])
    b = np.array(data["b"])
    n = len(A)
    L = np.eye(n)  # Matriz identidad para L
    U = np.zeros((n, n))
    
    
    for j in range(n):
        for i in range(j, n):  # Calcular elementos de U
            U[j, i] = A[j, i] - sum(L[j, k] * U[k, i] for k in range(j))
        for i in range(j + 1, n):  # Calcular elementos de L
            L[i, j] = (A[i, j] - sum(L[i, k] * U[k, j] for k in range(j))) / U[j, j]

    # Sustitución progresiva para resolver Ly = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, k] * y[k] for k in range(i))

    # Sustitución regresiva para resolver Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i, k] * x[k] for k in range(i + 1, n))) / U[i, i]

    return JsonResponse({
            "L": L.tolist(),
            "U": U.tolist(),
            "x": x.tolist()
        })

import numpy as np
from django.http import JsonResponse
import json

def cholesky(request):
    data = json.loads(request.body)
    A = np.array(data["A"])
    b = np.array(data["b"])
    n = A.shape[0]
    L = np.eye(n, dtype=float)
    U = np.eye(n, dtype=float)

    # Factorización de Cholesky
    for i in range(n - 1):
        L[i, i] = np.sqrt(A[i, i] - np.dot(L[i, :i], U[:i, i]))
        U[i, i] = L[i, i]

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
            U[i, j] = (A[i, j] - np.dot(L[i, :i], U[:i, j])) / L[i, i]

    # Último paso para la diagonal
    L[n - 1, n - 1] = np.sqrt(A[n - 1, n - 1] - np.dot(L[n - 1, :n - 1], U[:n - 1, n - 1]))
    U[n - 1, n - 1] = L[n - 1, n - 1]

    # Sustitución progresiva
    L_b = np.hstack((L, b.reshape(-1, 1)))
    z = sustprgr(L_b)

    # Sustitución regresiva
    U_z = np.hstack((U, z.reshape(-1, 1)))
    x = sustregr(U_z)
    
    return JsonResponse({
            "L": L.tolist(),
            "U": U.tolist(),
            "x": x.tolist()
        })


def jacobi(request):
    data = json.loads(request.body)
    A = np.array(data["A"])
    b = np.array(data["b"])
    x0 = np.array(data["x0"])
    tolerance = data["tolerance"]
    N = data["N"]

    table = []  # Inicializamos la tabla para guardar iteraciones
    D = np.diag(np.diag(A))
    LU = A - D
    D_inv = np.linalg.inv(D)
    T = np.dot(-D_inv, LU)
    C = np.dot(D_inv, b)

    # Calcular el radio espectral
    eigenval = np.linalg.eigvals(T)
    spectral_radius = max(abs(eigenval))

    # Inicialización de iteraciones
    x = x0
    for i in range(N):
        x_temp = x
        x = np.dot(D_inv, np.dot(-LU, x)) + C
        error_absoluto = np.linalg.norm(x - x_temp)

        # Guardar en la tabla: iteración, error, solución actual
        table.append({
            "iter": i + 1,
            "E": "{:.5e}".format(error_absoluto),
            "x": x.tolist()
        })

        if error_absoluto < tolerance:
            return JsonResponse({
                "T": T.tolist(),
                "C": C.tolist(),
                "spectral_radius": spectral_radius,
                "table": table
            })

    return JsonResponse({
        "T": T.tolist(),
        "C": C.tolist(),
        "spectral_radius": spectral_radius,
        "table": table
    })


def seidel(request):
    try:
        data = json.loads(request.body)
        A = np.array(data["A"])
        b = np.array(data["b"])
        x0 = np.array(data["x0"])
        tolerance = data["tolerance"]
        N = data["N"]
        xant = np.array(x0, dtype=float)
        D = np.diag(np.diag(A))
        L = -np.tril(A, -1)
        U = -np.triu(A, 1)
        T = np.linalg.inv(D - L).dot(U)
        spectral_radius = np.max(np.abs(np.linalg.eigvals(T)))
        C = np.linalg.inv(D - L).dot(b)
        E = 1000
        cont = 0
        table = []

        while E > tolerance and cont < N:
            xact = T.dot(xant) + C
            E = np.linalg.norm(xact - xant)
            xant = xact
            cont += 1
            table.append([cont, "{:.5e}".format(E), xant.tolist()])

        return JsonResponse({
            "T": T.tolist(),
            "C": C.tolist(),
            "table": table,
            "spectral_radius": spectral_radius
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
def SOR(request):
    data = json.loads(request.body)
    A = np.array(data["A"])
    b = np.array(data["b"])
    x0 = np.array(data["x0"])
    tolerance = data["tolerance"]
    w = data["w"]
    N = data["N"]
    xant = np.array(x0, dtype=float)

    D = np.diag(np.diag(A))
    L = -np.tril(A, -1) 
    U = -np.triu(A, 1)
    
    T = np.linalg.inv(D - w * L).dot((1 - w) * D + w * U)
    spectral_radius = np.max(np.abs(np.linalg.eigvals(T)))
    C = w * np.linalg.inv(D - w * L).dot(b)
    
    E = 1000
    cont = 0
    table = []

    while E > tolerance and cont < N:
        xact = T.dot(xant) + C
        E = np.linalg.norm(xact - xant)
        xant = xact
        cont += 1
        
        table.append([cont, "{:.5e}".format(E), xant.tolist()])

    return JsonResponse({
        "T": T.tolist(),
        "C": C.tolist(),
        "table": table,
        "spectral_radius": spectral_radius
    })
   
    
def vandermonde(x):
    n = len(x)
    V = np.vander(x)
    print("Vandermonde matrix:")
    for row in V:
        formatted_row = " ".join(f"{elem:.6f}" for elem in row)
        print(formatted_row)
    return V


def difdivididas(request): 
    try:
        data = json.loads(request.body)
        X = np.array(ast.literal_eval(data["x"]), dtype=float)
        Y = np.array(ast.literal_eval(data["y"]), dtype=float)

        if len(X) != len(Y) or len(X) < 2:
            raise ValueError("X and Y must have the same length, and at least 2 points are required.")
        
        n = len(X)
        
        # Initialize the divided difference table
        D = np.zeros((n, n))
        D[:, 0] = Y  # First column is just Y values

        # Compute divided differences
        for j in range(1, n):
            for i in range(n - j):
                D[i + j, j] = (D[i + j, j - 1] - D[i + j - 1, j - 1]) / (X[i + j] - X[i])

        # Extract the coefficients (first row of the table)
        Coef = D.diagonal().tolist()

        # Create a lower triangular table
        D_lower = np.zeros_like(D)
        for i in range(n):
            for j in range(i + 1):
                D_lower[i, j] = D[i, j]

        # Construct Newton's polynomial
        polynomial = f"{Coef[0]:.6f}"
        for i in range(1, len(Coef)):
            term = f"{Coef[i]:+.6f}"
            for k in range(i):
                term += f"(x-{X[k]:.6f})"
            polynomial += " " + term

        return JsonResponse({
            "divided_difference_table": D_lower.tolist(),
            "newton_coefficients": Coef,
            "newton_polynomial": polynomial,
            "message": "Divided differences computed successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def lagrange(request):
    try:
        data = json.loads(request.body)
        X = np.array(ast.literal_eval(data["x"]), dtype=float)
        Y = np.array(ast.literal_eval(data["y"]), dtype=float)

        if len(X) != len(Y) or len(X) < 2:
            raise ValueError("X and Y must have the same length, and at least 2 points are required.")
        n = len(X)

        # Initialize the Lagrange basis polynomials
        L = np.zeros((n, n))

        # Construct Lagrange basis polynomials
        for i in range(n):
            aux0 = np.delete(X, i)
            aux = np.array([1.0])

            # Construct the polynomial L_i(x) for each i
            for xj in aux0:
                aux = np.convolve(aux, [1, -xj])  # Multiply by (x - xj)

            # Normalize L_i(x) so that L_i(X[i]) = 1
            L[i, :] = (aux / np.polyval(aux, X[i])).tolist() + [0] * (n - len(aux))

        # Compute the coefficients of the interpolating polynomial
        Coef = Y @ L

        # Construct the interpolating polynomial
        polynomial = " + ".join(f"{Coef[i]:.6f}*L{i}" for i in range(n))

        return JsonResponse({
            "lagrange_basis_polynomials": L.tolist(),
            "interpolating_polynomial": polynomial,
            "message": "Lagrange interpolation computed successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
def trazlin(request):
    try:
        data = json.loads(request.body)
        X = np.array(ast.literal_eval(data["x"]), dtype=float)
        Y = np.array(ast.literal_eval(data["y"]), dtype=float)

        if len(X) != len(Y) or len(X) < 2:
            raise ValueError("X and Y must have the same length, and at least 2 points are required.")

        # Calculate the coefficients for each segment
        coefficients = []
        trazadores = []  # Lista para almacenar las ecuaciones de los trazadores
        for i in range(len(X) - 1):
            # Compute slope (m) and intercept (b) for each segment
            m = (Y[i+1] - Y[i]) / (X[i+1] - X[i])
            b = Y[i] - m * X[i]
            coefficients.append([m, b])
            
            # Crear ecuación del trazador en formato y = mx + b
            trazador = f"{m:.6f}x + {b:.6f}"
            trazadores.append(trazador)

        return JsonResponse({
            "coefficients": coefficients,
            "splines": trazadores,
            "message": "Linear interpolation computed successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)



def trazcuad(request):
    try:
        data = json.loads(request.body)
        X = np.array(ast.literal_eval(data["x"]), dtype=float)
        Y = np.array(ast.literal_eval(data["y"]), dtype=float)

        n = len(X)
        m = 3 * (n - 1)
        A = np.zeros((m, m))
        b = np.zeros(m)

        # Interpolation conditions
        for i in range(n - 1):
            A[i, 3 * i:3 * i + 3] = [X[i + 1]**2, X[i + 1], 1]
            b[i] = Y[i + 1]
        A[n - 1, 0:3] = [X[0]**2, X[0], 1]
        b[n - 1] = Y[0]

        # Continuity conditions
        for i in range(1, n - 1):
            A[n - 1 + i, 3 * i - 3:3 * i + 3] = [X[i]**2, X[i], 1, -X[i]**2, -X[i], -1]
            b[n - 1 + i] = 0

        # Smoothness conditions
        for i in range(1, n - 1):
            A[2 * (n - 1) - 1 + i, 3 * i - 3:3 * i + 3] = [2 * X[i], 1, 0, -2 * X[i], -1, 0]
            b[2 * (n - 1) - 1 + i] = 0

        # Boundary condition for the quadratic spline (second derivative zero at endpoints)
        A[-1, 0] = 2
        b[-1] = 0

        # Solve the system
        try:
            Saux = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            return JsonResponse({"error": "Singular matrix detected."})

        # Organize output coefficients and splines
        Coef = []
        Splines = []
        for i in range(n - 1):
            a, b, c = Saux[3 * i:3 * i + 3]
            Coef.append([a, b, c])
            trazador = f"{a:.6f}x^2 + {b:.6f}x + {c:.6f}"
            Splines.append(trazador)

        return JsonResponse({
            "method": "Quadratic Splines",
            "coefficients": Coef,
            "splines": Splines,
            "message": "Quadratic spline interpolation computed successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

def trazcub(request):
    try:
        # Example input data
        data = json.loads(request.body)
        X = np.array(ast.literal_eval(data["x"]), dtype=float)
        Y = np.array(ast.literal_eval(data["y"]), dtype=float)
        n = len(X)
        m = 4 * (n - 1)

        A = np.zeros((m, m))
        b = np.zeros(m)

        # Interpolation conditions (fitting the splines to points)
        row = 0
        for i in range(n - 1):
            A[row, 4 * i:4 * i + 4] = [X[i]**3, X[i]**2, X[i], 1]
            b[row] = Y[i]
            row += 1
            A[row, 4 * i:4 * i + 4] = [X[i + 1]**3, X[i + 1]**2, X[i + 1], 1]
            b[row] = Y[i + 1]
            row += 1

        # Continuity conditions (ensuring derivatives match between segments)
        for i in range(1, n - 1):
            A[row, 4 * (i - 1):4 * (i + 1)] = [
                3 * X[i]**2, 2 * X[i], 1, 0,
                -3 * X[i]**2, -2 * X[i], -1, 0
            ]
            b[row] = 0
            row += 1

        # Smoothness conditions (ensuring second derivatives match between segments)
        for i in range(1, n - 1):
            A[row, 4 * (i - 1):4 * (i + 1)] = [
                6 * X[i], 2, 0, 0,
                -6 * X[i], -2, 0, 0
            ]
            b[row] = 0
            row += 1

        # Natural spline boundary conditions (second derivative is zero at endpoints)
        A[row, 0:2] = [6 * X[0], 2]
        b[row] = 0
        row += 1
        A[row, -4:-2] = [6 * X[-1], 2]
        b[row] = 0

        # Solve the system
        try:
            Saux = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            return JsonResponse({"error": "Singular matrix detected."})

        # Organize output coefficients and splines
        Coef = []
        Splines = []
        for i in range(n - 1):
            a, b, c, d = Saux[4 * i:4 * i + 4]
            Coef.append([a, b, c, d])
            trazador = f"{a:.6f}x^3 + {b:.6f}x^2 + {c:.6f}x + {d:.6f}"
            Splines.append(trazador)

        return JsonResponse({
            "method": "Cubic Splines",
            "coefficients": Coef,
            "splines": Splines,
            "message": "Cubic spline interpolation computed successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
