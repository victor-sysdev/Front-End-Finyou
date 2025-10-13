from django.shortcuts import render
from django.http import HttpResponse

# Criando as Views

def home(request):
    return render(request, "home.html")
