from django.contrib import admin
from .models import Category, Product, Favorites, Review

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
    filter_vertical = ['items']

admin.site.register(Favorites, SavedItems)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['product', 'user', 'body']
