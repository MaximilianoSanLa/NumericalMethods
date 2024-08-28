from django.urls import path
from . import views

urlpatterns = [
    path('', views.Calculator, name='Calculator'),  # La ruta raíz para la app Calculator
    path('funcion/', views.funcion, name="funcion")
]