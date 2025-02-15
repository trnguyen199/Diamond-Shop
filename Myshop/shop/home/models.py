from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name
# Create your models here.
