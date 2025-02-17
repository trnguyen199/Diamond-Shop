# home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    # path('view_cart/', views.view_cart, name='view_cart'),
]
