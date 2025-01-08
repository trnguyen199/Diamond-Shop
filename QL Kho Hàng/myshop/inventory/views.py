from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Product

# Cập nhật hàng tồn kho
def update_inventory(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Tìm sản phẩm hoặc trả về lỗi 404
    if request.method == 'POST':
        try:
            new_quantity = int(request.POST.get('quantity', 0))
            product.stock_quantity = new_quantity
            product.save()
            return HttpResponseRedirect('/inventory/view-inventory/')  # Chuyển hướng sau khi cập nhật
        except ValueError:
            return render(request, 'inventory/update_inventory.html', {
                'error': 'Vui lòng nhập số hợp lệ!',
                'product': product
            })
    return render(request, 'inventory/update_inventory.html', {'product': product})

# Xem hàng tồn kho
def view_inventory(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm
    return render(request, 'inventory/view_inventory.html', {'products': products})

# Báo cáo hàng hết/thiếu
def low_stock_report(request):
    threshold = int(request.GET.get('threshold', 5))  # Ngưỡng cảnh báo
    low_stock_products = Product.objects.filter(stock_quantity__lte=threshold)
    return render(request, 'inventory/low_stock_report.html', {'products': low_stock_products})

# Trang chủ
def home(request):
    return render(request, 'inventory/home.html')  # Đường dẫn tới template
