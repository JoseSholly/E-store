from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from django.contrib import messages
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm


# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart= Cart(request)
    product= get_object_or_404(Product, id=product_id)
    form= CartAddProductForm(request.POST)
    if form.is_valid():
        cd= form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
        messages.success(request,
                         f"Item added to cart successfully")

    return redirect('cart:cart_detail')
    
@require_POST
def cart_remove(request, product_id):
    cart= Cart(request)
    product= get_object_or_404(Product, id= product_id)
    cart.remove(product)
    messages.success(request,
                         f"Item removed from cart successfully")

    return redirect('cart:cart_detail')

def cart_detail(request):
    cart= Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})

    return render(request, 
                  'cart/detail.html',
                  {'cart': cart})
