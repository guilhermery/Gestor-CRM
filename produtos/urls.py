from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('novo', views.adicionar_produto, name='novo')
]
