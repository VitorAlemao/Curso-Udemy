
from django.shortcuts import get_list_or_404, render

from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'pages/home.html', context={
        'receitas': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id'))

    return render(request, 'pages/category.html', context={
        'receitas': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })


def receita(request, id):
    recipe = Recipe.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    return render(request, 'pages/receitas-view.html', context={
        'receita': recipe,
        'is_detail_page': True,
    })
