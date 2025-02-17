from django.shortcuts import render
from .models import Product

def cart_view(request):
    # Lấy tất cả sản phẩm trong giỏ hàng
    products = Product.objects.all()  # Hoặc có thể sử dụng .filter() nếu cần lọc theo điều kiện nào đó

    # Tính tổng tiền cho từng sản phẩm
    for product in products:
        product.tongtien = product.gia * product.soluong

    # Truyền dữ liệu vào context
    context = {
        'products': products
    }

    return render(request, 'home/cart.html', context)

def get_home(request):
    return render(request, 'home/home.html')  # Template home.html cần có













# home/views.py
# from django.shortcuts import render, redirect
# from .models import Product

# Create your views here.
# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart = request.session.get('cart', {})
    
#     if product.id in cart:
#         cart[product.id]['quantity'] += 1
#     else:
#         cart[product.id] = {
#             'name': product.name,
#             'price': str(product.price),
#             'quantity': 1
#         }
    
#     request.session['cart'] = cart
#     return redirect('view_cart')  # Đảm bảo đã định nghĩa URL view_cart

# # home/views.py
# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     if product_id in cart:
#         del cart[product_id]
    
#     request.session['cart'] = cart
#     return redirect('view_cart')  # Trở lại trang giỏ hàng

# # home/views.py
# # def update_cart(request, product_id):
# #     cart = request.session.get('cart', {})
# #     quantity = int(request.POST.get('quantity', 1))  # Lấy số lượng từ form
    
# #     if product_id in cart:
# #         if quantity > 0:
# #             cart[product_id]['quantity'] = quantity
# #         else:
# #             del cart[product_id]  # Nếu số lượng = 0, xóa sản phẩm khỏi giỏ
    
# #     request.session['cart'] = cart
# #     return redirect('view_cart')

# def add_product():
#     pass

# def remove_product():
#     pass

# # home/views.py
# def view_cart(request):
#     cart = request.session.get('cart', {})
#     total = sum(float(item['price']) * item['quantity'] for item in cart.values())
#     return render(request, 'home/home.html', {'cart': cart, 'total': total})

