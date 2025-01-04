from django.shortcuts import get_object_or_404
from .models import Order

def create_order_logic(customer, total_price, notes):
    """
    Tạo một đơn hàng mới.
    """
    order = Order.objects.create(
        customer=customer,
        total_price=total_price,
        notes=notes
    )
    return order

def edit_order_logic(order_id, customer, total_price=None, notes=None):
    """
    Chỉnh sửa thông tin đơn hàng.
    """
    order = get_object_or_404(Order, id=order_id, customer=customer)

    if order.status != 'Pending':
        raise ValueError("Chỉ có thể chỉnh sửa đơn hàng chưa xử lý.")

    if total_price:
        order.total_price = total_price
    if notes:
        order.notes = notes
    order.save()
    return order

def cancel_order_logic(order_id, customer):
    """
    Hủy đơn hàng.
    """
    order = get_object_or_404(Order, id=order_id, customer=customer)

    if order.status != 'Pending':
        raise ValueError("Chỉ có thể hủy đơn hàng chưa xử lý.")

    order.status = 'Cancelled'
    order.save()
    return order
