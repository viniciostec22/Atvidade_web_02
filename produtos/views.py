from email import message
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Produto, Categoria
from .forms import ProdutoModelForm

def index(request):
    return render(request, 'produtos/index.html')

def produtos(request):
    
    produtos = Produto.objects.all()
    paginator = Paginator(produtos, 10)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'produtos/produtos.html', {'produtos': produtos})

def add_produto(request):
    forms = ProdutoModelForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        messages.add_message(request,messages.SUCCESS,'Produto salvo com sucesso!')
        return redirect('produtos')
    return render(request, 'produtos/add_edit_produto.html', {'forms': forms})

def edit_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    form = ProdutoModelForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,f'{produto.nome.upper()} editado(a) com sucesso!')
        return redirect('produtos')
    return render(request, 'produtos/add_edit_produto.html', {'produto': produto, 'forms': form})

def del_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method=="POST":
        produto.delete()
        messages.add_message(request,messages.SUCCESS,f'{produto.nome.upper()} excluído(a) com sucesso!')
    return redirect('produtos')

def categorias(request):

    categorias = Categoria.objects.all()
    paginator = Paginator(categorias, 10)
    page = request.GET.get('page')
    categorias = paginator.get_page(page)

    return render(request, 'produtos/categorias.html', {'categorias': categorias})

def sobre(request):
    return render(request, 'produtos/sobre.html')
