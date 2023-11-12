from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .models import Favorites
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
# Create your views here.

def product_list(request, category_slug=None):
    category= None
    categories= Category.objects.all()
    products= Product.objects.filter(available=True)
    if category_slug:
        category= get_object_or_404(Category, 
                                    slug= category_slug)
        products= products.filter(category=category)

    return render(request, 
                'shop/product/list.html',
                {'catogory': category,
                'categories': categories,
                'products': products,})


def product_detail(request, id, slug):
    product= get_object_or_404(Product,
                               id=id,
                               slug=slug,
                               available=True)
    cart_product_form= CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form},)



# @login_required
# def toggle_favorite(request, product_id):
#     user= request.user
#     favorite_items, created= Favorites.objects.get_or_create(user=user)
#     product = get_object_or_404(Product, pk=product_id)

#     if product in favorite_items.items.all():
#         favorite_items.items.remove(product)
#         messages.success(request, f"Item removed to favorites")
#         is_favorite = False
#     else:
#         favorite_items.items.add(product)
#         messages.success(request, f"Item added to favorites")
#         is_favorite = True

#     print(f"Item ID: {product_id}, Is Favorite: {is_favorite}")

#     # return redirect('shop:product_detail')
#     return JsonResponse({'is_favorite': is_favorite})

@login_required
def toggle_favorite(request, product_id):
    print("Toggle Favorite View Called")
    user = request.user
    favorite_items, created = Favorites.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)

    if product in favorite_items.items.all():
        print("Item Removed from Favorites")
        favorite_items.items.remove(product)
        messages.success(request, f"Item removed to favorites")
        is_favorite = False
    else:
        print("Item Added to Favorites")
        favorite_items.items.add(product)
        messages.success(request, f"Item added to favorites")
        is_favorite = True

    return JsonResponse({'is_favorite': is_favorite})

    

