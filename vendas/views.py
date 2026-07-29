from django.shortcuts import render
from .models import Venda

def vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/ver_vendas.html', {'vendas':vendas})

def adicionar_venda(request):
    pass

def detalhes_venda(request):
    pass

def excluir_venda(request):
    pass