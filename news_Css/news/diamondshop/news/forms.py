from django import forms
from .models import NewsArticle

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'short_description', 'description', 'image']
from django import forms
from .models import NewsArticle

class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'short_description', 'description', 'image']

    # Cấu hình để form hỗ trợ upload file
    image = forms.ImageField(required=False)
