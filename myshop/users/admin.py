from django.contrib import admin
from .models import CustomProfile, CustomUser

# Register your models here.
# admin.site.register(CustomProfile)
# admin.site.register(CustomUser)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display= ["email", "first_name", "last_name", "is_active"]
    list_filter= ['date_joined', 'first_name' ]

@admin.register(CustomProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display= ['user', 'image', 'date_of_birth', 'phone_number']
    list_filter= ['user']
