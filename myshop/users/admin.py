from django.contrib import admin
from .models import CustomProfile, CustomUser

# Register your models here.
admin.site.register(CustomProfile)
admin.site.register(CustomUser)