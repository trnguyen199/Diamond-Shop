from django.shortcuts import render, redirect
from django.http import HttpResponse
from page.models import Category, Product, contactForm
from django.views.decorators.csrf import csrf_exempt
import json
from page.models import Category,Order
from .form import ProductForm ,CategoryForm
# Create your views here.

def diamondshop(request):
    return render(request, 'home.html')

def qldanhmuc(request):
    categories = Category.objects.all() 
    return render(request, 'home/qldanhmuc.html', {'categories': categories})

def qlsanpham(request):
    products = Product.objects.all() 
    return render(request, 'home/qlsanpham.html', {'products': products})
def qltaikhoan(request):
    users =  contactForm.objects.all() 
    return render(request, 'home/qltaikhoan.html', {'users': users})
def qldonhang(request):
    orders =  Order.objects.all() 
    return render(request, 'home/qldonhang.html', {'orders': orders})
def qllienhe(request):
    contacts =  contactForm.objects.all() 
    return render(request, 'home/qllienhe.html', {'contacts': contacts})

def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('add_category') 
    return render(request, 'home/qldanhmuc.html')

def add_product(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')  # Load lại trang sau khi thêm
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form, 'categories': categories})



@csrf_exempt
def update_category(request, category_id):
    print(f"🔍 DEBUG: Nhận request update cho category ID {category_id}")  # Debug log

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("📨 Dữ liệu nhận được:", data)  # Debug log

            from home.models import Category  # Import tại đây tránh lỗi circular import

            category = Category.objects.get(id=category_id)
            category.name = data.get("name", category.name)
            category.save()

            print("✅ Cập nhật thành công!")
            return JsonResponse({"success": True})
        except Category.DoesNotExist:
            return JsonResponse({"success": False, "error": "Danh mục không tồn tại!"})
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Dữ liệu JSON không hợp lệ!"})
    else:
        return JsonResponse({"success": False, "error": "Yêu cầu không hợp lệ!"})
