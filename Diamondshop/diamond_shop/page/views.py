from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .form import contact_Form
from  .models import *
#product models
from django.views.generic import ListView, DetailView
from page.models import Category, Product, Customer
from django.http import JsonResponse
import json
from .models import Product, Order, OrderItem  
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .form import ChangePasswordForm

def home(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'home-page/product.html')

def contact(request):
    context = {'cf': contact_Form}    
    return render(request, 'home-page/contact.html', context)

def introduction(request):
    return render(request, 'home-page/introduction.html')

def discount(request):
    return render(request, 'home-page/discount.html')

def profile(request):
    return render(request, 'home-page/profile.html')

@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data["new_password"]
            request.user.set_password(new_password)  # Cập nhật mật khẩu
            request.user.save()
            update_session_auth_hash(request, request.user)  # Giữ phiên đăng nhập
            messages.success(request, "Mật khẩu đã được thay đổi thành công.")
            return redirect("page:getProfile")  # Chuyển hướng về trang hồ sơ
    else:
        form = ChangePasswordForm(request.user)

    return render(request, "home-page/profile.html", {"form": form})


@login_required
def getProfile(request):
    customer, created = Customer.objects.get_or_create(user=request.user)

    if request.method == "POST":
        fullname = request.POST.get("fullname", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()

        if fullname and phone and address:
            # Cập nhật thông tin
            customer.fullname = fullname
            customer.phone = phone
            customer.address = address
            customer.save()
        return redirect("page:getProfile")
    return render(request, "home-page/profile.html", {"customer": customer})













def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'home-page/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'home-page/checkout.html', context)

def news(request):
    return render(request, 'home-page/news.html')

def getContact(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return redirect('/contact')  # Chuyển hướng về trang contact
    return render(request, 'contact.html')  # Load trang contact nếu không phải POST

class HomeListView(ListView):
    model = Product
    template_name = 'home-page/product.html'
    context_object_name = 'products'
    

def product_view(request):
    category_id = request.GET.get('category', None)

    if category_id:  
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all() 

    return render(request, 'product.html', {'products': products})

def get_product_detail(request):
    product_id = request.GET.get('id')
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product-detail.html', {'product': product})


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action', action)
    print('productID', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Sản phẩm đã được thêm', safe= False)