from django.db import models

# Create your models here.
from django.db import models

# Tạo model sản phẩm (Product)
class Product(models.Model):
    name = models.CharField(max_length=100)  # Tên sản phẩm
    price_purchase = models.DecimalField(max_digits=10, decimal_places=0)  # Giá nhập
    price_selling = models.DecimalField(max_digits=10, decimal_places=0)  # Giá bán
    quantity = models.PositiveIntegerField()  # Số lượng trong kho
    quantity_sold = models.PositiveIntegerField(default=0)  # Số lượng đã bán
