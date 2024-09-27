from django.urls import path
from . import views

urlpatterns = [
    path('', views.Calculator, name='Calculator'),
    path("fun_bisection/", views.fun_bisection, name="fun_bisection"),
    path("graph_function/", views.graph_function, name= "graph_function"),
    path("newton_method/", views.newton, name="newton_method")
]