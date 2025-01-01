from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('<int:order_id>/edit/', views.edit_order, name='edit_order'),
    path('<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
]
