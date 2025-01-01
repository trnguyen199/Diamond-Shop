from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Chưa xử lý'),
        ('Processing', 'Đang xử lý'),
        ('Completed', 'Hoàn tất'),
        ('Cancelled', 'Đã hủy'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"
