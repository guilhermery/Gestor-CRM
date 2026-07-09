from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def listar_clientes(request):
    
    return render(request, 'listar_clientes.html')

def adicionar_cliente(request):
    return HttpResponse('Oii')