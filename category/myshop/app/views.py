from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Product
from .forms import CategoryForm, ProductForm

# 🏠 Trang Chủ
def home_view(request):
    categories = Category.objects.all()
    return render(request, 'app/base.html', {'categories': categories})

# Danh sách danh mục
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app/category_list.html', {'categories': categories})

# Thêm danh mục
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Danh mục đã được thêm thành công!")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'app/add_category.html', {'form': form})

# Cập nhật danh mục
def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Cập nhật danh mục thành công!")
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'app/update_category.html', {'form': form})

# Xóa danh mục
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "🗑️ Danh mục đã bị xóa!")
        return redirect('category_list')
    return render(request, 'app/delete_category.html', {'category': category})

# Danh sách sản phẩm
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'app/product_list.html', {'products': products})

#  Thêm sản phẩm
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Sản phẩm đã được thêm thành công!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'app/add_product.html', {'form': form})

# Cập nhật sản phẩm
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, " Cập nhật sản phẩm thành công!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app/update_product.html', {'form': form})

#  Xóa sản phẩm
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, " Xóa sản phẩm thành công!")
        return redirect('product_list')
    return render(request, 'app/delete_product.html', {'product': product})
