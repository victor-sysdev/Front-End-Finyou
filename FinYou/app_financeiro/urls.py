from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home, login, recuperarSenha, teste, pagamento, criarConta
from .forms import Formulario_Login

urlpatterns = [
    path("", home, name="rota_home"),
    path("login/", login, name="rota_login", ),
    path("criarConta/", criarConta, name="rota_criarConta"),
    path("recuperarSenha/", recuperarSenha, name="rota_recuperarSenha"),
    path("teste/", teste, name="rota_teste"),
    path("pagamento/", pagamento, name="rota_pagamento"),
    
    ]