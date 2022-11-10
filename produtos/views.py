from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Produto, Categoria
from .forms import ProdutoModelForm, CategoriaModelForm
from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from django.db.models import Q


def index(request):
    return render(request, 'produtos/index.html')

def produtos(request):
    if request.GET.get('termo'):
        termo = request.GET.get('termo')
        produtos = Produto.objects.filter(Q(nome__icontains=termo) | Q(preco__icontains=termo) | Q(descricao__icontains=termo))
    else:
        produtos = Produto.objects.order_by('-id')
    
    paginator = Paginator(produtos, 10)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'produtos/produtos.html', {'produtos': produtos})

def add_produto(request):
    if request.method == 'GET':
        forms = ProdutoModelForm()
        return render(request, 'produtos/add_edit_produto.html', {'forms': forms})
    else:
        forms = ProdutoModelForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.add_message(request,messages.SUCCESS,'Produto salvo com sucesso!')
            return redirect('produtos')
        return render(request, 'produtos/add_edit_produto.html', {'forms': forms})  

def edit_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        forms = ProdutoModelForm(request.POST, request.FILES, instance=produto)
        if forms.is_valid():
            forms.save()
            messages.add_message(request,messages.SUCCESS,f'{produto.nome.upper()} editado(a) com sucesso!')
            return redirect('produtos')
    else:
        forms = ProdutoModelForm(instance=produto)
    return render(request, 'produtos/add_edit_produto.html', {'produto': produto, 'forms': forms})
       
def del_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method=="POST":
        produto.delete()
        messages.add_message(request,messages.SUCCESS,f'{produto.nome.upper()} excluído(a) com sucesso!')
    return redirect('produtos')

def categorias(request):
    if request.GET.get('termo'):
        termo = request.GET.get('termo')
        categorias = Categoria.objects.filter(Q(nome__icontains=termo))
    else:
        categorias = Categoria.objects.order_by('nome')

    categorias = Categoria.objects.all()
    paginator = Paginator(categorias, 10)
    page = request.GET.get('page')
    categorias = paginator.get_page(page)

    return render(request, 'produtos/categorias.html', {'categorias': categorias})

def sobre(request):
    return render(request, 'produtos/sobre.html')

def deleteCategoria(request, categoria_id):
    categoria = get_object_or_404( Categoria, id=categoria_id)
    #categoria = Categoria.objects.get(id=categoria_id)
    if request.method=="POST":
        categoria.delete()
        messages.add_message(request,messages.SUCCESS,f'{categoria.nome.upper()} excluído(a) com sucesso!')
    return redirect('categorias')

def edit_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        forms = CategoriaModelForm(request.POST, request.FILES, instance=categoria)
        if forms.is_valid():
            forms.save()
            messages.add_message(request,messages.SUCCESS,f'{categoria.nome.upper()} editado(a) com sucesso!')
            return redirect('categorias')
    else:
        forms = CategoriaModelForm(instance=categoria)
    return render(request, 'produtos/add_edit_categoria.html', {'categoria': categoria, 'forms': forms})
   

def add_categoria(request):
    if request.method == 'GET':
        forms = CategoriaModelForm()
        return render(request, 'produtos/add_edit_categoria.html', {'forms': forms})
    else:
        forms = CategoriaModelForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.add_message(request,messages.SUCCESS,'Categoria salva com sucesso!')
            return redirect('categorias')
        return render(request, 'produtos/add_edit_categoria.html', {'forms': forms})
   