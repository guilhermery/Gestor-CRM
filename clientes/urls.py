from django.contrib import admin
from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('novo/', views.adicionar_cliente, name="novo"),
    path('<int:cliente_id>/', views.detalhes_cliente, name="detalhes"),
    path('<int:cliente_id>/editar/', views.editar_cliente, name="editar"),
    path('<int:cliente_id>/excluir/', views.excluir_cliente, name="excluir")
]