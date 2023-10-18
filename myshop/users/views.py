from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            username= form.cleaned_data.get('first_name')
            messages.success(
                request, f"{username}, Your account has created successfully. You can login now!"
            )
            return redirect(reverse(f"shop:product_list"))
    else:
        form= UserRegisterForm()
    return render(request, 
                  'users/register.html', 
                  {'form': form})

def user_login(request):
    if request.method=='POST':
        form= AuthenticationForm(data= request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect(reverse(f"shop:product_list"))
    else:
        form= AuthenticationForm()
    return render(request,
                  'users/login.html',
                  {'form': form})

