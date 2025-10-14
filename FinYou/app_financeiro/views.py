from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.urls import reverse_lazy

# Criando as Views

def home(request):
    return render(request, "app_financeiro/home.html")

def login(request):
    return render(request, "app_financeiro/login.html")

def criarConta(request):
    return render(request, "app_financeiro/nova_conta.html")

def recuperarSenha(request):
    return render(request, "app_financeiro/recuperacao.html")

def dashboard(request):
    return render(request, "teste.html")

def pagamento(request):
    return HttpResponse("<h1>Página de pagamento</h1>")
