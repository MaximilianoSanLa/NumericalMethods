from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import metodo
import math
import io
import matplotlib.pyplot as plt
import numpy as np

def Calculator(request):
    nombre = metodo.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        "first_name": nombre[0].x
    }
    return HttpResponse(template.render(context, request))

def funcion(request):
    fig, ax = plt.subplots()
    x = np.arange(10.0)
    ax.plot(x)
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return HttpResponse(buffer, content_type="image/png")