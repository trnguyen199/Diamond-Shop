from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_product/', views.add_product, name='add_product'),
    # path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('list_products/', views.list_products, name='list_products'),
    path('search/', views.search_product, name='search_product'),
]