from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .models import Favorites, Review
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .forms import ReviewForm, SearchForm
from django.views.decorators.http import require_POST
from django.urls import reverse
from .recommender import Recommender
from django.contrib.postgres.search import SearchVector
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
    reviews= Review.objects.filter(product= id)
    cart_product_form= CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    
    # if request.method== "POST":
    #     review_form= ReviewForm(request.POST)
    #     if review_form.is_valid():
    #         review= review_form.save(commit=False)
    #         review.user= request.user
    #         review.product= product
    #         review.save()

    #         return redirect('shop:product_detail', id= id, slug= slug)
    # else:
    #     review_form= ReviewForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'reviews': reviews,
                   'recommended_products': recommended_products},)



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
    # print("Toggle Favorite View Called")
    user = request.user
    favorite_items, created = Favorites.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)

    if product in favorite_items.items.all():
        # print("Item Removed from Favorites")
        favorite_items.items.remove(product)
        is_favorite = False
        # print(f"Item removed to Wishlist")
        messages.success(request, f"Item removed to Wishlist")
    else:
        # print("Item Added to Favorites")
        favorite_items.items.add(product)
        is_favorite = True
        # print(f"Item added to Wishlist")
        messages.success(request, f"Item added to Wishlist")

    return JsonResponse({'is_favorite': is_favorite})

    

@require_POST
def post_review(request, id, slug):
    product= get_object_or_404(Product,
                               id=id,
                               slug=slug,
                               available=True)
    review= None

    # review instantiated
    form= ReviewForm(data= request.POST)

    if form.is_valid():
        # Creating review object without saving 
        review= form.save(commit=False)
        # Assigns product to review
        review.product= product

        review.user= request.user

        # Save review to database
        review.save()



    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'review_form': form,
                   'review': review})


def post_search(request):
    form = SearchVector()
    query= None
    results= []

    if 'query' in request.GET:
        form = SearchVector(request.GET)
        if form.is_valid():
            query= form.cleaned_data['query']
            results= Product.objects.annotate(search= SearchVector('name')).filter(search= query)

    return render(request,
                  'shop/product/search.html',
                  {'form': form,
                    'query': query,
                    'results': results})
