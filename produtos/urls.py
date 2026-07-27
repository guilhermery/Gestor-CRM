from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "produtos"

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('novo', views.adicionar_produto, name='novo'),
    path('<int:produto_id>', views.detalhes_produto, name='detalhes'),
    path('<int:produto_id>/editar', views.detalhes_produto, name='detalhes'),
    path('<int:produto_id>/excluir', views.detalhes_produto, name='detalhes'),
]
