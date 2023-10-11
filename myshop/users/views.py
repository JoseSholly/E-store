from django.shortcuts import render, redirect, 
from django.contrib.auth import login
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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

