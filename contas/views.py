from django.shortcuts import redirect, render

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    
    return render(request, 'cadastro.html')

def logout(request):
    return redirect('login')