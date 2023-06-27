from django.shortcuts import render


# Create your views here.
# HTTP Request
def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Ingrid Esteves'})
    # return HTTP Response


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'name': 'Ingrid Esteves'})
    # return HTTP Response
