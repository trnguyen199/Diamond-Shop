from django.urls import path
from .views import home_view, category_list, add_category, update_category, delete_category, product_list, add_product, update_product, delete_product

urlpatterns = [
    path('', home_view, name='home'),

    # Quản lý danh mục
    path('categories/', category_list, name='category_list'),
    path('categories/add/', add_category, name='add_category'),
    path('categories/update/<int:category_id>/', update_category, name='update_category'),
    path('categories/delete/<int:category_id>/', delete_category, name='delete_category'),

    # Quản lý sản phẩm
    path('products/', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
    path('products/update/<int:product_id>/', update_product, name='update_product'),
    path('products/delete/<int:product_id>/', delete_product, name='delete_product'),
]
