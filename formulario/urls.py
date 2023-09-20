from django.urls import path 
from . import views

from django.conf import settings

urlpatterns = [
    path('calcular_valores', views.calcular_valores, name='calcular'),
]
