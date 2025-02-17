# home/models.py
from django.db import models

class Product(models.Model):
    sanpham = models.CharField(max_length=255)
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    soluong = models.IntegerField()
    tongtien = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.sanpham
