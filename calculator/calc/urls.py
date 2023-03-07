from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator),
    path("as/", views.calculadora_cuadratica)
]
