from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('add-inventory/', views.add_inventory, name='add-inventory'),
    path('recipes/', views.recipes, name='recipes'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('register/', views.register, name='register'),
]