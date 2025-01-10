from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Locker_Api import views as locker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locker_views.home, name='home'),
    path('dashboard/', locker_views.dashboard, name='dashboard'),
    path('inventory/', locker_views.inventory, name='inventory'),
    path('add-inventory/', locker_views.add_inventory, name='add-inventory'),
    path('recipes/', locker_views.recipes, name='recipes'),
    path('add-recipe/', locker_views.add_recipe, name='add-recipe'),
    path('register/', locker_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Locker_Api/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Locker_Api/logout.html'), name='logout'),
]