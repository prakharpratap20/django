from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")
    else:
        form = RegistrationForm()
        
    return render(request, "authentication/register.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(username=username, password=password).first()
            if user:
                messages.success(request, "Login Successful.")
                return redirect("Home")
            else:
                messages.error(request, "Invalid Login credentials.")
    else:
        form = LoginForm()
    
    return render(request, "authentication/login.html", {"form": form})