from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from .services import create_order_logic, edit_order_logic, cancel_order_logic
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'orders/login.html'



@login_required
def create_order(request):
    if request.method == 'POST':
        total_price = request.POST.get('total_price')
        notes = request.POST.get('notes')

        try:
            order = create_order_logic(
                customer=request.user,
                total_price=total_price,
                notes=notes
            )
            messages.success(request, f"Đơn hàng #{order.id} đã được tạo thành công!")
            return redirect('create_order')
        except Exception as e:
            messages.error(request, f"Lỗi: {str(e)}")

    return render(request, 'orders/create_order.html')

@login_required
def edit_order(request, order_id):
    if request.method == 'POST':
        total_price = request.POST.get('total_price')
        notes = request.POST.get('notes')

        try:
            order = edit_order_logic(
                order_id=order_id,
                customer=request.user,
                total_price=total_price,
                notes=notes
            )
            messages.success(request, f"Đơn hàng #{order.id} đã được cập nhật.")
            return redirect('edit_order', order_id=order.id)
        except Exception as e:
            messages.error(request, f"Lỗi: {str(e)}")

    order = get_object_or_404(Order, id=order_id, customer=request.user)
    return render(request, 'orders/edit_order.html', {'order': order})

@login_required
def cancel_order(request, order_id):
    try:
        order = cancel_order_logic(order_id=order_id, customer=request.user)
        messages.success(request, f"Đơn hàng #{order.id} đã được hủy.")
    except Exception as e:
        messages.error(request, f"Lỗi: {str(e)}")

    return redirect('create_order')

class CustomLoginView(LoginView):
    template_name = 'orders/login.html'
@login_required
def view_order(request, order_id):
    # Lấy thông tin đơn hàng dựa trên ID và khách hàng hiện tại
    order = get_object_or_404(Order, id=order_id, customer=request.user)

    # Trả về trang view_order.html với dữ liệu của đơn hàng
    return render(request, 'orders/view_order.html', {'order': order})


def create_order(request):
    return render(request, 'orders/create_order.html')

def cancel_order(request, order_id):
    return render(request, 'orders/cancel_order.html')

def edit_order(request, order_id):
    return render(request, 'orders/edit_order.html')

def view_order(request, order_id):
    return render(request, 'orders/view_order.html')
def home(request):
    return render(request, 'home.html')