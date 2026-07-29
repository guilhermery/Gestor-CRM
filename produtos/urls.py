from django.contrib import admin
from django.urls import path
from . import views

app_name = "produtos"

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('novo', views.adicionar_produto, name='novo'),
    path('<int:produto_id>', views.detalhes_produto, name='detalhes'),
    path('<int:produto_id>/editar', views.editar_produto, name='editar'),
    path('<int:produto_id>/excluir', views.excluir_produto, name='excluir'),
]