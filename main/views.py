from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    return render(request, 'main.html')

def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.filter(name=name, password=password).first()
        if user:
            request.session['user_id'] = user.id
            messages.success(request, "Signed in successfully.")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        if CustomUser.objects.filter(name=name).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'signup.html')
        CustomUser.objects.create(name=name, email=email, password=password)
        messages.success(request, "Account created successfully. Please sign in.")
        return redirect('signin')
    return render(request, 'signup.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')