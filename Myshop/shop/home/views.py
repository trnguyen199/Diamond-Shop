from django.shortcuts import render

# Create your views here.
def get_home (request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse

# Thêm sản phẩm
def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        price = float(request.POST['price'])
        Product.objects.create(name=name, category=category, price=price)
        return redirect('list_products')
    return render(request, 'pages/add_product.html')

# Chỉnh sửa sản phẩm
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.price = float(request.POST['price'])
        product.save()
        return redirect('list_products')
    return render(request, 'home/edit_product.html', {'product': product})

# Xóa sản phẩm
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('list_products')

# Liệt kê sản phẩm
def list_products(request):
    products = Product.objects.all()
    return render(request, 'pages/list_products.html', {'products': products})

# Tìm kiếm sản phẩm
def search_product(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query) | Product.objects.filter(category__icontains=query)
    return render(request, 'home/search_results.html', {'products': products, 'query': query})

def index(request):
    return render(request, 'index.html')