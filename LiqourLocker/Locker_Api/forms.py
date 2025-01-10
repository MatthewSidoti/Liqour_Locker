from django import forms
from .models import Product, DrinkRecipe, Inventory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'category', 'quantity', 'price', 'description']
        widgets = {
            'sku': forms.TextInput(attrs={'placeholder': 'Enter SKU number'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'})
        }

class DrinkRecipeForm(forms.ModelForm):
    class Meta:
        model = DrinkRecipe
        fields = ['name', 'ingredients', 'instructions', 'image']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity', 'min_quantity']