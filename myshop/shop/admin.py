from django.contrib import admin
from .models import Category, Product, Favorites

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name', 'slug']
    prepopulated_fields= {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['name', 'slug', 'price', 'available', 'created', 'stock_quantity', 'updated']
    list_filter= ['available', 'created', 'updated']
    list_editable=['price', 'available']
    prepopulated_fields= {'slug': ('name',)}

class SavedItems(admin.ModelAdmin):
    list_display= ['user']
    filter_horizontal = ['items']
admin.site.register(Favorites, SavedItems)