from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/ver_produtos.html', {'produtos': produtos})

def adicionar_produto(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        Produto.objects.create(
            nome = nome,
            descricao = descricao,
            preco = preco,
            quantidade = quantidade
        )
        return redirect('produtos')
    return render(request, 'produtos/adicionar_produtos.html')

def detalhes_produto(request):
    produtos = Produto.objects.all()
    return render(request, 'detalhes_produto.html', {'produtos': produtos})