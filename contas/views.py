from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib.auth.models import User
import re

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=senha)
        if not user:
            messages.add_message(request,messages.ERROR,'Usuario ou senha incorretos!')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        messages.add_message(request,messages.SUCCESS,'Login efetuado com sucesso!')
        return render(request,'produtos/index.html')
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        senha = request.POST.get('senha')
        repita_senha = request.POST.get('repita_senha')
        
        user = User.objects.filter(username=usuario)
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            messages.add_message(request,messages.ERROR,'email invalido!') 
        elif senha != repita_senha:
            messages.add_message(request,messages.ERROR,'Senhas não são iguais!') 
            return redirect('cadastro')
        elif  senha < '8':
            messages.add_message(request,messages.ERROR,'Senha muito curta!') 
            return redirect('cadastro')
        elif user.exists():
            messages.add_message(request,messages.ERROR,'Usuario já cadastrado!') 
            return redirect('cadastro')
        
        elif not usuario or not nome or not sobrenome or not senha or not repita_senha:
            messages.add_message(request,messages.ERROR,'não pode dexar campos em branco!')
            return redirect('cadastro')
        
        #user = User.objects.create_user(username=usuario, email=email, first_name=nome, last_name=sobrenome, password=senha)  # type: ignore
        #messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!') 
        #return redirect('cadastro')
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))