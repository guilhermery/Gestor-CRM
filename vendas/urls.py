from django.contrib import admin
from django.urls import path
from . import views

app_name = "vendas"

urlpatterns = [
    path('', views.vendas, name='vendas'),
    path('novo', views.adicionar_venda, name='novo'),
    path('<int:produto_id>', views.detalhes_venda, name='detalhes'),
    path('<int:produto_id>/excluir', views.excluir_venda, name='excluir'),
]