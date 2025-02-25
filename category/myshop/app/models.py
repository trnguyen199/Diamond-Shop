from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Tên danh mục")
    slug = models.SlugField(unique=True, blank=True)
    is_sub = models.BooleanField(default=False, verbose_name="Là danh mục con?")
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='subcategories', on_delete=models.CASCADE, verbose_name="Danh mục cha"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Danh mục"
        verbose_name_plural = "Danh mục"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tên sản phẩm")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Danh mục")
    price_new = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Giá mới")  # 🔥 Thêm default=0.0
    price_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Giá cũ")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Hình ảnh")
    created_at = models.DateTimeField(default=now, verbose_name="Ngày tạo")  
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sản phẩm"
        verbose_name_plural = "Sản phẩm"
