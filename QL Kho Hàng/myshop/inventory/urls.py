from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('view-inventory/', views.view_inventory, name='view_inventory'),
    path('low-stock-report/', views.low_stock_report, name='low_stock_report'),
    path('update-inventory/<int:product_id>/', views.update_inventory, name='update_inventory'),
]
