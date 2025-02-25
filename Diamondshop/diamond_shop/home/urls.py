from django.contrib import admin
from django.urls import include, path
from home import views
from .views import update_category

app_name = 'page_mg'

urlpatterns = [
    path('diamondshop', views.diamondshop, name = "diamondshop"),
    path('qldanhmuc/', views.qldanhmuc, name = "qldanhmuc"),
    path('aaaa/update/<int:category_id>/', update_category, name='update_category'),
    path('qlsanpham/', views.qlsanpham, name = "qlsanpham"),
    path('qltaikhoan/', views.qltaikhoan, name = "qltaikhoan"),
    path('qldonhang/', views.qldonhang, name = "qldonhang"),
    path('qllienhe/', views.qllienhe, name = "qllienhe"),
    path('add-category/', views.add_category, name='add_category'),
    path('add-product/', views.add_product, name='add_product'),
    
]