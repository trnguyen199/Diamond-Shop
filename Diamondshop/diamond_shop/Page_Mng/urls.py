from django.urls import path
from . import views

urlpatterns = [
    path('Pageh/', views.User, name='Pageh'),
    
]