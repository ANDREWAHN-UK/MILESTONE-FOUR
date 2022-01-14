from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404
    )
from wishlist.models import Wishlist, WishlistItem
from profiles.models import UserProfile

from store.models import Product
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.contrib import messages

# Create your views here.
""" 
Much googling and research led to the following:
https://github.com/pigmonkey/django-wishlist
https://www.youtube.com/watch?v=OgA0TTKAtqQ&ab_channel=VeryAcademy

Code below is based on that, and on the following Slack conversation:

https://code-institute-room.slack.com/archives/C7HS3U3AP/p1613310583353100

and documentation here:
https://docs.djangoproject.com/en/3.1/topics/db/models/#intermediary-manytomany


"""


@login_required
def wishlist(request):
    """ A view to show an existing wishlist """
    items = []
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]
    existingWishlist = WishlistItem.objects.filter(
        wishlist=wishlist_user).exists()

    if existingWishlist:
        user_wishlist = get_list_or_404(WishlistItem, wishlist=wishlist_user)
        for obj in user_wishlist:
            product = get_object_or_404(Product, name=obj)
            items.append(product)
        context = {
            'wishlist': True,
            'products': items
        }
        return render(request, 'wishlist/wishlist.html', context)

    else:
        context = {
            'wishlist': False,
        }
        return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add a item in the Wishlist """
    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    product = Product.objects.get(pk=product_id, quantity=1)
    if request.POST:
        existingWishlistItem = WishlistItem.objects.filter(
            wishlist=wishlist_user, product=product).exists()
        if existingWishlistItem:
            messages.error(request, f'{product.name} already in your wishlist!')
            return redirect(redirect_url)

        else:
            added_item = WishlistItem(
                wishlist=wishlist_user,
                product=product,
                date_added=timezone.now()
                )
            added_item.save()
            messages.success(request, f'{product.name} added to your wishlist!')
            return redirect(redirect_url)
    else:
        messages.error(request, "Click 'Add to wishlist' to add a item ")
        return render(request, 'home.html')


@login_required
def remove_from_wishlist(request, product_id):
    """ A view to delete a item in the wishlist"""

    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
   
    if request.POST:
        product = Product.objects.get(pk=product_id, quantity=1)

        # look for item in the user's wishlistItem - returns true if it exists
        existingWishlistItem = WishlistItem.objects.filter(
            product=product).exists()

        if existingWishlistItem:
            product = WishlistItem.objects.get(product=product)
            product.delete()
            messages.success(request, "Item removed from wishlist")
            return redirect(redirect_url)

        if existingWishlistItem is None:
            messages.error(
                request, "You can not delete a item thats not in the wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, 'Item can not be deleted from your wishlist')
        return render(request, 'home.html')
        