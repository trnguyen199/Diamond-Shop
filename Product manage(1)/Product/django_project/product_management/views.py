from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product  # Import model Product

# Tạo sản phẩm mới
def product_create(request):
    if request.method == "POST":
        name = request.POST['name']
        price_purchase = float(request.POST['purchase_price'])
        price_selling = float(request.POST['selling_price'])
        quantity = int(request.POST['quantity'])

        # Lưu sản phẩm vào database
        item_product = Product(
            name=name,
            price_purchase=price_purchase,
            price_selling=price_selling,
            quantity=quantity
        )
        item_product.save()

        # Thông báo khi thêm thành công
        messages.success(request, 'Sản phẩm đã được tạo thành công!')

        return redirect('product_list')  # Chuyển hướng về danh sách sản phẩm

    return render(request, 'product_create.html', {})

# Hiển thị danh sách sản phẩm
def product_list(request):
    items_product = Product.objects.all()
    return render(request, 'product_list.html', {'items_product': items_product})


# Cập nhật sản phẩm
def product_update(request, product_id):
    item_product = Product.objects.get(id=product_id)  # Lấy sản phẩm từ database

    if request.method == "POST":
        name = request.POST['name']
        price_purchase = float(request.POST['purchase_price'])
        price_selling = float(request.POST['selling_price'])
        quantity = int(request.POST['quantity'])
        quantity_sold = int(request.POST['sold_quantity'])  # Đã sửa lỗi: lấy đúng "sold_quantity"

        # Cập nhật trực tiếp vào sản phẩm hiện có
        item_product.name = name
        item_product.price_purchase = price_purchase
        item_product.price_selling = price_selling
        item_product.quantity = quantity
        item_product.quantity_sold = quantity_sold  # Đã sửa lỗi

        item_product.save()  # Lưu thay đổi vào database
 
        
        messages.success(request, 'Sản phẩm đã được cập nhật thành công!')

        return redirect('/')  # Chuyển hướng về danh sách sản phẩm

    return render(request, 'product_update.html', {'item_product': item_product})

def product_delete(request, product_id):
    item_product = Product.objects.get(id=product_id)  # Lấy sản phẩm từ database
    item_product.delete()  # Xóa sản phẩm

    # Thông báo xóa thành công
    messages.success(request, 'Sản phẩm đã được xóa thành công!')