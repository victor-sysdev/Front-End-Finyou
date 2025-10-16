from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

# Etapas de configuração de autenticação dos usuários
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Importação de arquivos locais
from .forms import Formulario_Login, Formulario_Criar_Conta

# Criando as Views
def home(request):
    user = request.user #Pego o usuário atual, com base no usuário da requisição
    if user.is_authenticated: #Verifica se o usuário está autenticado
        return render(request, "app_financeiro/home.html", context={"user":user})
        #return HttpResponse(f"O usuário {User.get_username} está cadastrado")
    else:
        #return HttpResponse(f"Você não está autenticado")
        return render(request, "app_financeiro/home.html")

def criarConta(request):
    if request.method == "GET":
        return render(
            request,
            "app_financeiro/criar_conta.html",
            {"Formulario_Criar_Conta": Formulario_Criar_Conta()},
        )
    else:
        form = Formulario_Criar_Conta(
            request.POST
        )  # Acessando os dados passados pelo meu formuçário
        if form.is_valid():  # Verificando se o formulário foi preenchido corretamente
            # pegando as informações do formulário
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Verificando se o usuário já está cadastrado (com base no username e no email)
            user = User.objects.filter(username=username, email=email).exists()
            if user:
                return HttpResponse(
                    f"Usuario {username} já foi criado, entre em sua conta"
                )
            # Criando o Usuario
            else:
                print("Usuario criado agora")
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                return HttpResponse(f"{username}, {email}, {password}")

def login(request):
    if request.method == "GET":
        return render(request, "app_financeiro/login.html", {"Formulario_Login": Formulario_Login()},
        )

    else:
        form = Formulario_Login(
            request.POST
        )  # Inicializa uma instancia do formulário com base nos dados passados pelo formulario
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]  # NÃO UTILIZADA ATÉ O MOMENTO

            # Verificando se o usuario existe
            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                if user:
                    auth_login(request, user=user)
                    return HttpResponse(
                        f"Pode fazer login - O usuario {user} foi autenticado"
                    )
                else:
                    return HttpResponse(f"Você não foi autenticado")
            else:
                return render(request, "rota_hone")
                #return HttpResponse("O usuário não existe, crie-o")

def recuperarSenha(request):
    return render(request, "app_financeiro/recuperacao.html")

@login_required(login_url="rota_login")
def logout(request):
    ...

@login_required(login_url="rota_login")
def dashboard(request):
    #user = User.objects.get(username=username)
    return render(request, "app_financeiro/auxilhoFinyou.html")

@login_required(login_url="rota_login")
def pagamento(request):
    return render(request, "app_financeiro/pagamento.html")