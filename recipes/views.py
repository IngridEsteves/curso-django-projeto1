from django.shortcuts import render


# Create your views here.
# HTTP Request
def home(request):
    return render(request, 'recipes/home.html')
    # return HTTP Response