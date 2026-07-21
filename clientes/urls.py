from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('detalhes_cliente', views.detalhes_cliente, name="detalhes"),
    path('editar_cliente', views.editar_cliente, name="editar"),
    path('adicionar_cliente', views.adicionar_cliente, name="adicionar"),
    path('excluir_cliente', views.excluir_cliente, name="excluir")
]