from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)  # Tiêu đề bài viết
    short_description = models.TextField()  # Mô tả ngắn
    description = models.TextField()  # Nội dung chi tiết
    image = models.ImageField(upload_to='news_images/')  # Hình ảnh
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo

    def __str__(self):
        return self.title
