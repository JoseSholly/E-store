from django import forms
from .models import CustomProfile, CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    class Meta:
        model= CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields= ['email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomProfile
        exclude= ['updated']