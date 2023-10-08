from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as lazy

# Create your models here.
class CustomUser(AbstractUser):
    username= None
    email= models.EmailField(lazy('email address'), unique=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    def __str__(self) -> str:
        return  self.email
