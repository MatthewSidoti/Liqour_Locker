from django import forms
from .models import Product, DrinkRecipe, Inventory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity', 'price', 'description']

class DrinkRecipeForm(forms.ModelForm):
    class Meta:
        model = DrinkRecipe
        fields = ['name', 'ingredients', 'instructions', 'image']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity', 'min_quantity']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']