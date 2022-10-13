
from django.shortcuts import render
from Utils.receitas.Factory import make_recipe

from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'pages/home.html', context={
        'receitas': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'pages/home.html', context={
        'receitas': recipes,
    })


def receita(request, id):
    return render(request, 'pages/receitas-view.html', context={
        'receita': make_recipe(),
        'is_detail_page': True,
    })
