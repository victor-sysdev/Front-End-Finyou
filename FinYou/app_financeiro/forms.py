from django import forms

class Formulario_Login(forms.Form):
    username = forms.CharField(required=True, label="Digite seu username", initial="Marcos")
    email = forms.EmailField()
    password = forms.CharField()

class Formulario_Criar_Conta(forms.Form):
    username = forms.CharField(required=True, label="Digite seu username", initial="Marcos")
    email = forms.EmailField(required=True, label="Digite seu email", initial="marcos@gmail.com")
    password = forms.CharField(required=False, label="Digite sua senha", widget=forms.PasswordInput(), initial=123)