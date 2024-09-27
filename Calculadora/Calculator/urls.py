from django.urls import path
from . import views

urlpatterns = [
    path('', views.Calculator, name='Calculator'),
    path("fun_bisection/", views.fun_bisection, name="fun_bisection"),
    path("regla_falsa_method/", views.regla_falsa_method, name="regla_falsa_method"),
    path("graph_function/", views.graph_function, name= "graph_function"),
    path("incremental_search_method/", views.incremental_search_method, name= "incremental_search_method"),
    path("newton_method/", views.newton, name="newton_method")
]