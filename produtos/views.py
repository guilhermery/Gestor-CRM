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
        return redirect('produtos:produtos')
    return render(request, 'produtos/adicionar_produtos.html')

def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('produtos:detalhes', produto.id)
    return render(request, 'produtos/editar_produto.html', {'produto': produto})

def detalhes_produto(request, produto_id):
    produto = Produto.objects.get(id = produto_id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})

def excluir_produto(request, produto_id):
    produto = Produto.objects.get(id = produto_id)
    produto.delete()
    return redirect('produtos:produtos')