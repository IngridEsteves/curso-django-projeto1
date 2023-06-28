from django.urls import path
from . import views


app_name = 'recipes'

# dominio/
urlpatterns = [
    path('', views.home, name="home"),  # home /
    path('recipes/<int:id>/', views.recipe, name="recipe"),  # /recipes/
]
