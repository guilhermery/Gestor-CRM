from django.shortcuts import render, redirect
from .models import Produto, Cliente, Venda

def index(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()

    total_clientes = clientes.count()
    total_produtos = produtos.count()
    total_vendas = vendas.count()

    faturamento = 0.0

    for venda in vendas:
        faturamento += venda.valor_total

    estoque_baixo = Produto.objects.filter(quantidade__lte=5)
    context = {'total_clientes': total_clientes, 'total_produtos': total_produtos, 'total_vendas': total_vendas, 'faturamento': faturamento, 'estoque_baixo': estoque_baixo}
    return render(request, 'core/index.html', context)