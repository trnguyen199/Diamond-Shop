from django.urls import path
from .views import news_list, news_detail, news_create, news_update, news_delete

urlpatterns = [
    path('', news_list, name='home'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('create/', news_create, name='news_create'),
    path('update/<int:pk>/', news_update, name='news_update'),
    path('delete/<int:pk>/', news_delete, name='news_delete'),
]
