from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, DrinkRecipe, Inventory
from .forms import ProductForm, DrinkRecipeForm, InventoryForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'Locker_Api/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Locker_Api/register.html', {'form': form})

@login_required
def dashboard(request):
    inventory_count = Inventory.objects.count()
    low_stock_count = Inventory.objects.filter(quantity__lte=5).count()
    context = {
        'inventory_count': inventory_count,
        'low_stock_count': low_stock_count,
    }
    return render(request, 'Locker_Api/dashboard.html', context)

@login_required
def inventory(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'Locker_Api/inventory.html', {'inventory': inventory_items})

@login_required
def recipes(request):
    recipes = DrinkRecipe.objects.all()
    return render(request, 'Locker_Api/recipes.html', {'recipes': recipes})

@login_required
def product_list(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'Locker_Api/product_list.html', {'products': products, 'form': form})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = DrinkRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipes')
    else:
        form = DrinkRecipeForm()
    return render(request, 'Locker_Api/add_recipe.html', {'form': form})

@login_required
def edit_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'Locker_Api/edit_inventory.html', {'form': form, 'item': item})

@login_required
def delete_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory')
    return render(request, 'Locker_Api/delete_inventory.html', {'item': item})