from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('This is a bad request. Start with the music route.')

def music(request):
    return HttpResponse('blues')

def artist1(request):
    return HttpResponse('Muddy Waters')

def artist2(request):
    return HttpResponse('Fats Domino')

def artist3(request):
    return HttpResponse('B.B. King')