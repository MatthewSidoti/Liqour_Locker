from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, DrinkRecipe, Inventory
from .forms import DrinkRecipeForm, InventoryForm
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
    recipes = DrinkRecipe.objects.all()[:4]
    context = {
        'inventory_count': inventory_count,
        'low_stock_count': low_stock_count,
        'recipes': recipes,
    }
    return render(request, 'Locker_Api/dashboard.html', context)

@login_required
def inventory(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'Locker_Api/inventory.html', {'inventory': inventory_items})

@login_required
def add_inventory(request):
    if request.method == 'POST':
        sku = request.POST.get('sku')
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        
        
        product = Product.objects.create(
            sku=sku,
            name=name,
            category=category
        )
        
        
        Inventory.objects.create(
            product=product,
            quantity=quantity
        )
        
        messages.success(request, 'Item added successfully!')
        return redirect('inventory')
        
    return render(request, 'Locker_Api/add_inventory.html')

@login_required
def recipes(request):
    recipes = DrinkRecipe.objects.all()
    return render(request, 'Locker_Api/recipes.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = DrinkRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('recipes')
    else:
        form = DrinkRecipeForm()
    return render(request, 'Locker_Api/add_recipe.html', {'form': form})