from django.contrib import admin
from django.urls import include, path
from . import views
from .views import updateItem

app_name = 'page'

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('product/', views.HomeListView.as_view(), name = "product"),
    path('contact/', views.contact, name = "contact"),
    path('introduction/', views.introduction, name = "introduction"),
    path('discount/', views.discount, name = "discount"),
    path('profile/', views.profile, name = "profile"),
    path('getProfile/', views.getProfile, name="getProfile"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('contact/', views.contact, name = "contact"),
    path('news/', views.news, name = "news"),
    path('getContact/', views.getContact, name = "getContact"),
    path('get-product-detail/', views.get_product_detail, name='get_product_detail'),
    path('change-password/', views.change_password, name="change_password"),
]
