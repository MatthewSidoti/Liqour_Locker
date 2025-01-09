from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='liquor/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='liquor/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recipes/', views.drink_recipes, name='recipes'),
    path('recipes/add/', views.add_recipe, name='add_recipe'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/update/<int:pk>/', views.update_inventory, name='update_inventory'),
]