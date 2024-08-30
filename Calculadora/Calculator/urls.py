from django.urls import path
from . import views

urlpatterns = [
    path('', views.Calculator, name='Calculator'),
    path("fun_bisection/", views.fun_bisection, name="fun_bisection")
    
]