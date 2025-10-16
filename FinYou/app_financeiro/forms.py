from django import forms


class Formulario_Login(forms.Form):
    username = forms.CharField(
        required=True, label="Digite seu username", initial="Marcos"
    )
    email = forms.EmailField(
        required=True,
        label="Digite seu email",
    )
    password = forms.CharField(
        required=True,
        label="Digite sua senha",
        widget=forms.PasswordInput(),
    )


class Formulario_Criar_Conta(forms.Form):
    username = forms.CharField(
        required=True, 
        label="Digite seu username", 
    )
    email = forms.EmailField(
        required=True,
        label="Digite seu email",
    )
    password = forms.CharField(
        required=True,
        label="Digite sua senha",
        widget=forms.PasswordInput(),
    )
