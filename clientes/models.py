from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    telefone = models.IntegerField(default="0000000000")
    email = models.EmailField(default="")

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    preco = models.FloatField()
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome