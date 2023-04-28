from django.shortcuts import render


# Create your views here.
# HTTP Request
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP Response


# HTTP Request
def sobre(request):
    return render(request, 'recipes/sobre.html')  
    # return HTTP Response


# HTTP Request
def contato(request):
    return render(request, 'recipes/contato.html')
    # return HTTP Response