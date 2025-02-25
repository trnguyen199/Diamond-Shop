from django import forms
from .models import contactForm, Customer
from django.contrib.auth.forms import AuthenticationForm


class contact_Form(forms.ModelForm):
    class Meta:
        model = contactForm
        fields = ['username','address','email','phone' ,'content']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên khách hàng(*)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email(*)'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Điện thoại(*)'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'cols': 50 , 'placeholder': 'Nội dung liên hệ(*)'}),
        }           
        
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu cũ")
    new_password = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu mới")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Xác nhận mật khẩu")

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if not check_password(old_password, self.user.password):
            self.add_error("old_password", "Mật khẩu cũ không đúng.")

        if new_password != confirm_password:
            self.add_error("confirm_password", "Mật khẩu xác nhận không khớp.")

        return cleaned_data