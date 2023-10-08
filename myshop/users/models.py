from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as lazy
from birthday import BirthdayField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUser(AbstractUser):
    username= None
    email= models.EmailField(lazy('email address'), unique=True)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    date_of_birth= BirthdayField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    def __str__(self) -> str:
        return  self.email
    
class CustomProfile(models.Model):
    user= models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image= models.ImageField(upload_to= 'profile_pics')


    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} Profile"
