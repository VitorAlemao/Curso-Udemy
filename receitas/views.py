
from django.shortcuts import render
from Utils.receitas.Factory import make_recipe

# Create your views here.


def home(request):
    return render(request, 'pages/home.html', context={
        'receitas': [make_recipe for _ in range(10)],
    })


def receita(request, id):
    return render(request, 'pages/receitas-view.html', context={
        'receita': make_recipe(),
        'is_detail_page': True,
    })
