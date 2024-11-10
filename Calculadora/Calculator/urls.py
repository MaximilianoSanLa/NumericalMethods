from django.urls import path
from . import views

urlpatterns = [
    path('', views.Calculator, name='Calculator'),
    path("fun_bisection/", views.fun_bisection, name="fun_bisection"),
    path("regla_falsa_method/", views.regla_falsa_method, name="regla_falsa_method"),
    path("graph_function/", views.graph_function, name= "graph_function"),
    path("punto_fijo_method/", views.punto_fijo_method, name= "punto_fijo_method"),
    path("incremental_search_method/", views.incremental_search_method, name= "incremental_search_method"),
    path("newton_method/", views.newton_method, name="newton_method"),
    path("secant_method/", views.secant_method, name= "secant_method"),
    path("multiple_roots_method/", views.multiple_roots_method, name= "multiple_roots_method"),
    path("gausspl_method/", views.gausspl_method, name= "gausspl_method"),
    path("gausspar_method/", views.gausspar_method, name= "gausspar_method"),
    path("gausstot_method/", views.gausstot_method, name= "gausstot_method")
]