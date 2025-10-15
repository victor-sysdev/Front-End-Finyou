from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

#Etapas de configuração de autenticação dos usuários
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


# Criando as Views

def home(request):
    return render(request, "app_financeiro/home.html")

def login(request):
    if request.method == "GET":
        return render(request, "app_financeiro/login.html")
    else:
        return HttpResponse("Tá tirando")

def criarConta(request):
    return render(request, "app_financeiro/nova_conta.html")

def recuperarSenha(request):
    return render(request, "app_financeiro/recuperacao.html")

def dashboard(request):
    return render(request, "teste.html")

def pagamento(request):
    return HttpResponse("<h1>Página de pagamento</h1>")
