from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    telefone = models.IntegerField(default="0000000000")
    email = models.EmailField(default="")

    def __str__(self):
        return self.nome