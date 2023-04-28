from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# HTTP Request
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP Response


# HTTP Request
def sobre(request):
    return HttpResponse('SOBRE')
    # return HTTP Response


# HTTP Request
def contato(request):
    return HttpResponse('CONTATO')
    # return HTTP Response