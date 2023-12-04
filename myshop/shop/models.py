from django.db import models
from django.urls import reverse
from PIL import Image
from users.models import CustomUser
from django.core.exceptions import ValidationError
from decimal import Decimal
# from django_resized import ResizedImageField

# Model Discount validator
def validate_discount(value):
    if value < 0 or value > 100:
        raise ValidationError("Discount must be between 0 and 100.")
    else:
        return value
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering= ['name']
        indexes= [
            models.Index(fields=['name']),
        ]
        verbose_name= 'category'
        verbose_name_plural= 'categories'

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Product(models.Model):

    category= models.ForeignKey(Category, 
                                related_name='products', 
                                on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200)
    # image= ResizedImageField(scale=0.5, upload_to='products/%Y/%m/%d', blank= True)
    image= models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description= models.TextField(blank=True)
    price= models.DecimalField(max_digits=10, 
                               decimal_places=2)
    available= models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    stock_quantity= models.PositiveIntegerField()
    discount = models.IntegerField(default=0,
                                   validators=[validate_discount])


    class Meta:
        ordering= ['name']
        indexes= [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])

        ]
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id,
                             self.slug])
    def get_discount(self):
        actual_cost= self.price
        discount_price =actual_cost * (self.discount / Decimal(100))
        if self.discount:
            return actual_cost - discount_price
        return Decimal(0)



    


class Favorites(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items= models.ManyToManyField('shop.Product', 
                                     related_name='saved_items', blank=True)
    
    class Meta:
        ordering= ['user']
        indexes=[
            models.Index(fields=['user'])
        ]
        verbose_name= 'Saved Item'
        verbose_name_plural= 'Saved Items'
    def __str__(self) -> str:
        return f"{self.user.first_name} saved items"

class Review(models.Model):
    product= models.ForeignKey(Product, 
                               on_delete= models.CASCADE,
                               related_name='reviews')
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_name= models.CharField(max_length=255, blank=True)
    user_email= models.CharField(blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def user_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    def user_email(self):
        return f"{self.user.email}"
    class Meta:
        ordering = ['-created']
        indexes = [
        models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Review by {self.user.first_name} {self.user.email}'
    