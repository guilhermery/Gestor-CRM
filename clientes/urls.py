from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('novo/', views.adicionar_cliente, name="novo"),
    path('<int:cliente_id>/', views.detalhes_cliente, name="detalhes"),
    path('<int:cliente_id>/editar/', views.editar_cliente, name="editar"),
    path('excluir/<int:cliente_id>/', views.excluir_cliente, name="excluir")
]