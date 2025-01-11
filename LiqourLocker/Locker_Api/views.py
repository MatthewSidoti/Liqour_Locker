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
def add_inventory(request):
    if request.method == 'POST':
        sku = request.POST.get('sku')
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        
        # Create product first
        product = Product.objects.create(
            sku=sku,
            name=name,
            category=category
        )
        
        # Then create inventory entry
        Inventory.objects.create(
            product=product,
            quantity=quantity
        )
        
        messages.success(request, 'Item added successfully!')
        return redirect('inventory')
        
    return render(request, 'Locker_Api/add_inventory.html')

@login_required
def edit_inventory(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        sku = request.POST.get('sku')
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        
        # Update product
        inventory_item.product.sku = sku
        inventory_item.product.name = name
        inventory_item.product.category = category
        inventory_item.product.save()
        
        # Update inventory
        inventory_item.quantity = quantity
        inventory_item.save()
        
        messages.success(request, 'Item updated successfully!')
        return redirect('inventory')
        
    context = {
        'item': inventory_item
    }
    return render(request, 'Locker_Api/edit_inventory.html', context)

@login_required
def delete_inventory(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        inventory_item.product.delete()  # This will also delete the inventory item due to CASCADE
        messages.success(request, 'Item deleted successfully!')
        return redirect('inventory')
        
    context = {
        'item': inventory_item
    }
    return render(request, 'Locker_Api/delete_inventory.html', context)

@login_required
def recipes(request):
    recipes = DrinkRecipe.objects.all().order_by('-created_at')
    return render(request, 'Locker_Api/recipes.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        recipe_url = request.POST.get('recipe_url')
        image = request.FILES.get('image')
        
        recipe = DrinkRecipe.objects.create(
            name=name,
            recipe_url=recipe_url,
            image=image,
            created_by=request.user
        )
        
        messages.success(request, 'Recipe added successfully!')
        return redirect('recipes')
        
    return render(request, 'Locker_Api/add_recipe.html')