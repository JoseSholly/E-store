from django.db import models
from shop.models import Product
import uuid
from decimal import Decimal
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from coupons.models import Coupon
import re


# Creating Validators
def postal_code_validator(postal_code):

    # Check if postal code is alphanumeric and Check if postal code length is between 4 and 10 characters
    if len(postal_code) > 4 and re.match(r"^[0-9a-zA-Z]+$", postal_code):
        return postal_code
    else:
        raise ValidationError("Invalid Postal Code Format")


def validate_discount(value):
    if value < 0 or value > 100:
        raise ValidationError("Discount must be between 0 and 100.")
    else:
        return value
    
# Create your models here.

class Order(models.Model):
    id= models.UUIDField(primary_key=True,
                               default=uuid.uuid4, 
                               editable=False,
                               )
    first_name= models.CharField(max_length=50,)
    last_name= models.CharField(max_length=50,)
    email= models.EmailField()
    address= models.CharField(max_length=250)
    postal_code= models.CharField(max_length=10,null=True,validators=[postal_code_validator])
    city= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    paid= models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon,
                               related_name="orders_coupon",
                               null=True,
                               blank=True,
                               on_delete= models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[validate_discount])
    stripe_id = models.CharField(max_length=250, blank=True)


    class Meta:
        ordering= ['-created']
        indexes= [
            models.Index(fields=['-created'])
        ]
    def __str__(self) -> str:
        return f"Order {self.id}"

    def get_total_cost(self):
        total_cost= self.get_total_cost_before_discount()
        return total_cost - self.get_discount()
    
    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_discount(self):
        total_cost= self.get_total_cost_before_discount()
        if self.discount:
            return total_cost * (self.discount / Decimal(100))
        return Decimal(0)
    

class OrderItem(models.Model):
    order= models.ForeignKey(Order,
                             related_name='items',
                             on_delete=models.CASCADE)
    product= models.ForeignKey(Product,
                               related_name='order_items',
                               on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,default=0)
    quantity= models.PositiveIntegerField(default=1)
    

    def __str__(self) -> str:
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity