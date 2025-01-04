from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.shortcuts import render

# Đăng ký người dùng
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Tự động đăng nhập sau khi đăng ký
            messages.success(request, 'Registration successful!')
            return redirect('home') 
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Đăng nhập người dùng
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

# Đăng xuất người dùng
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Quay về trang đăng nhập



def home(request):
    return render(request, 'users/home.html')
