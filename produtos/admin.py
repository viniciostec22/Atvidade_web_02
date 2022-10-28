from django.contrib import admin

from .models import Categoria, Produto

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id','nome','preco','descricao','categoria']
    list_display_links = ['id','nome']
    list_editable = ['descricao']
    

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)