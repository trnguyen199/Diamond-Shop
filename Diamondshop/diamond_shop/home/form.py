from django import forms
from page.models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'Category', 'preview_des', 'description', 'image', 'price', 'old_price', 'is_stock']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên sản phẩm'}),
            'Category': forms.Select(attrs={'class': 'form-control'}),
            'preview_des': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mô tả ngắn'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Mô tả chi tiết'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Giá sản phẩm'}),
            'old_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Giá cũ (nếu có)'}),
            'is_stock': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']