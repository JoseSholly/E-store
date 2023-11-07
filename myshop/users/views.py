from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, HttpResponse
from shop.models import Product

# from .models import Favorites
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

def user_logout(request):
    logout(request)
    
    messages.success(request, 'You have been successfully logged out.')
    
    return redirect('shop:product_list')

@login_required
def user_profile(request):
    if request.method== "POST":
        user_form= UserUpdateForm(request.POST, instance= request.user)
        profile_form= ProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance=request.user.customprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('users:profile')
    else:
        user_form= UserUpdateForm(instance=request.user)
        profile_form= ProfileUpdateForm(instance=request.user.customprofile)
    return render(request,
                  'users/profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

