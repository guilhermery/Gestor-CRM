from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})
        
def detalhes_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    return render(request, 'clientes/detalhes_cliente.html', {'cliente': cliente})

def editar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.idade = request.POST.get('idade')
        cliente.telefone = request.POST.get('telefone')
        cliente.email = request.POST.get('email')
        cliente.save()
        return redirect('clientes:detalhes', cliente.id)
    return render(request, 'clientes/editar_cliente.html', {'cliente': cliente})

def excluir_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id = cliente_id)
    cliente.delete()
    return redirect('clientes:clientes')

def adicionar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        Cliente.objects.create(
            nome=nome,
            idade=idade,
            telefone=telefone,
            email=email
        )
        return redirect('clientes:clientes')
    return render(request, 'clientes/adicionar_clientes.html')