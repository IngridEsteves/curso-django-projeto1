from django.urls import path
from recipes.views import home


# dominio/
urlpatterns = [
    path('', home), # home /
]