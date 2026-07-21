from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

# Create your views here.
def listar_clientes(request):
    if request.method == "GET":
        nome = 'Guilherme'
        return render(request, 'listar_clientes.html', {'nome': nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        clientes = Cliente.objects.filter(nome = nome)
        cliente = Cliente(nome = nome, idade = idade, telefone = telefone, email = email)
        cliente.save()
        if clientes.exists():
            return HttpResponse("Usuario já cadastrado")
        else:
            return HttpResponse("Usuario cadastrado")

def adicionar_cliente(request):
     return render(request, 'adicionar_clientes.html')