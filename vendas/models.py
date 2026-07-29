from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    valor_total = models.FloatField()
    data_venda = models.DateTimeField(auto_now_add=True)