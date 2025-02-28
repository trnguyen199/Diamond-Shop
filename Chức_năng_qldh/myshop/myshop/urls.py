"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from orders.views import home, create_order, edit_order, cancel_order, view_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Đường dẫn gốc sẽ trỏ tới view Home
    path('home/', home, name='home'),
    path('orders/create/', create_order, name='create_order'),
    path('orders/<int:order_id>/edit/', edit_order, name='edit_order'),
    path('orders/<int:order_id>/cancel/', cancel_order, name='cancel_order'),
    path('orders/<int:order_id>/view/', view_order, name='view_order'),
]

