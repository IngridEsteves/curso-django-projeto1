from django.urls import path
from recipes.views import home, contato, sobre


# dominio/
urlpatterns = [
    path('', home), # home /
    path('sobre/', sobre), # /sobre/
    path('contato/', contato), # /contato/
]