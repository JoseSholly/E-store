from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as lazy
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    # username = models.CharField(max_length=150, default='')
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        ordering= ['email']
        indexes=[
            models.Index(fields=['email'])
        ]
        verbose_name= 'user'
        verbose_name_plural= 'users'

    def __str__(self):
        return self.email
    
    
class CustomProfile(models.Model):
    class GenderStatus(models.TextChoices):
        MALE= 'M', 'Male'
        FEMALE= 'F', 'Female'


    user= models.OneToOneField(CustomUser,
                               on_delete=models.CASCADE,)

    gender= models.CharField(max_length=1,
                             choices=GenderStatus.choices,
                             default=GenderStatus.MALE)
    address= models.CharField(max_length=250,
                              null=True)
    
    image= models.ImageField(upload_to= 'profile_pics',
                             default= 'default.jpg')
    
    date_of_birth= models.DateField(null=True,
                                    blank=True)
    
    phone_number = PhoneNumberField(blank= True)

    updated= models.DateTimeField(auto_now=True,)

    class Meta:
        ordering= ['-updated']
        indexes=[
            models.Index(fields=['-updated'])
        ]
        verbose_name= 'profile'
        verbose_name_plural= 'profiles'

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} Profile"









