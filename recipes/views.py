from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Home')


def contact(request):
    return HttpResponse('Contato teste')


def about(request):
    return HttpResponse('Sobre')
