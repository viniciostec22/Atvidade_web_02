from ctypes import resize
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    imagem = models.FileField(upload_to="img_category/%Y/%m/%d/", blank=True,default='')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    img = models.FileField(upload_to="img_prod/%Y/%m/%d/", blank=True,default='')
    preco = models.FloatField()
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome