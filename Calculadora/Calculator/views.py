from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import metodo
import math
import io
import matplotlib.pyplot as plt
import numpy as np
import base64

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

    x = np.linspace(-10, 10, 400)
    
    try:
        y = eval(ecuacion)
    except Exception as e:
        return HttpResponse(f"Error al evaluar la función: {e}")

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label=f"y = {ecuacion}")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Gráfica de la función y = {ecuacion}")
    plt.legend()
    plt.grid(True)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    
    plt.close()
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    context = {'buffer': image_base64}

    return HttpResponse(template.render(context, request))
