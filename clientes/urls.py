from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ver_clientes', views.listar_clientes, name="ver_clientes"),
    path('adicionar_cliente', views.adicionar_cliente, name="inserir_cliente")
]
