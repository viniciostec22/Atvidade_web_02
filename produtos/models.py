from ctypes import resize
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.FloatField()
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome