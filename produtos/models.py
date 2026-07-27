from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome