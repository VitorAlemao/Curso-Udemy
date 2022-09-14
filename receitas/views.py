from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Essa é a pagina inicial')


def sobre(request):
    return HttpResponse('Essa pagina é sobre minha vida')


def contato(request):
    return HttpResponse('Essa pagina é sobre meu contato')
