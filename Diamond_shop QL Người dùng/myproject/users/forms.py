from django import forms
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('customer', 'Khách hàng'),
        ('admin', 'Quản trị viên'),
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Role")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
