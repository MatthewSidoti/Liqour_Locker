# LiqourLocker/urls.py
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Locker_Api import views as locker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locker_views.home, name='home'),
    path('dashboard/', locker_views.dashboard, name='dashboard'),
    path('recipes/', locker_views.recipes, name='recipes'),
    path('inventory/', locker_views.inventory, name='inventory'),
    path('login/', auth_views.LoginView.as_view(template_name='Locker_Api/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Locker_Api/logout.html'), name='logout'),
    path('register/', locker_views.register, name='register'),
    # Add new product URLs
    path('product-list/', locker_views.product_list, name='product-list'),
    path('add-recipe/', locker_views.add_recipe, name='add-recipe'),
    path('edit-inventory/<int:pk>/', locker_views.edit_inventory, name='edit-inventory'),
    path('delete-inventory/<int:pk>/', locker_views.delete_inventory, name='delete-inventory'),
]