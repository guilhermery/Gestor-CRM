from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})
        
def detalhes_cliente(request):
    pass

def editar_cliente(request):
    pass

def excluir_cliente(request):
    pass


def verificar_clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})
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
     return render(request, 'clientes/adicionar_clientes.html')