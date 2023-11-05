from django.contrib import admin
from .models import CustomProfile, CustomUser, Favorites

# Register your models here.
# admin.site.register(CustomProfile)
# admin.site.register(CustomUser)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display= ["email", "first_name", "last_name", "is_active"]
    list_filter= ['date_joined', 'first_name', 'last_name', ]
    search_fields=['email', 'first_name',]
    date_hierarchy='date_joined'



@admin.register(CustomProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display= ['user', 'gender','date_of_birth', 'phone_number']
    list_filter= ['gender', 'updated']
    ordering= ['updated']

# @admin.register(Favorites)
# class SavedItems(admin.ModelAdmin):
#     filter_horizontal = ['favorites']


class SavedItems(admin.ModelAdmin):
    list_display= ['user']
    filter_horizontal = ['favorites']


admin.site.register(Favorites, SavedItems)