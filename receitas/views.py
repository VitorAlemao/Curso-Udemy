
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/home.html')


def receitas(request, id):
    return render(request, 'pages/receitas-view.html')
