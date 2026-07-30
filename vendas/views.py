from django.shortcuts import render, redirect
from .models import Venda, Produto, Cliente

def vendas(request):
    vendas = Venda.objects.all().order_by("-data_venda")
    total_vendas = vendas.count()
    itens_vendidos = 0
    faturamento = 0
    for venda in vendas:
        itens_vendidos += venda.quantidade
        faturamento += venda.valor_total
    context = {'vendas': vendas, 'total_vendas': total_vendas, 'itens_vendidos': itens_vendidos, 'faturamento': faturamento}
    return render(request, 'vendas/ver_vendas.html', context)

def adicionar_venda(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    context = {'clientes': clientes, 'produtos': produtos}
    if request.method == 'POST':
        cliente = Cliente.objects.get(id = request.POST.get('cliente'))
        produto = Produto.objects.get(id = request.POST.get('produto'))
        quantidade = int(request.POST.get('quantidade'))
        if quantidade <= 0:
            context['erro'] = 'A quantidade deve ser maior que zero.'
            return render(request, 'vendas/adicionar_vendas.html', context)
        if quantidade > produto.quantidade:
            context['erro'] = 'Estoque insuficiente.'
            return render(request, 'vendas/adicionar_vendas.html', context)
        valor_total = produto.preco * quantidade
        Venda.objects.create(
            cliente = cliente,
            produto = produto,
            quantidade = quantidade,
            valor_total = valor_total
        )
        produto.quantidade -= quantidade
        produto.save()
        return redirect('vendas:vendas')
    return render(request, 'vendas/adicionar_vendas.html', context)

def detalhes_venda(request, venda_id):
    venda = Venda.objects.get(id = venda_id)
    return render(request, 'vendas/detalhes_venda.html', {'venda':venda})

def excluir_venda(request, venda_id):
    venda = Venda.objects.get(id = venda_id)
    venda.delete()
    return redirect('vendas:vendas')