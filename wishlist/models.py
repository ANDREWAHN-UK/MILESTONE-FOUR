from django.db import models
from profiles.models import UserProfile
from store.models import Product
# Create your models here.

class Wishlist(models.Model):
    """ this model is to link together the user and the item wished for """
    user = models.OneToOneField(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='wishlist')

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    """A  model to link the wishlist and the products. Many products can be on many wishlists"""
    # documentation on many to many :
    # https://docs.djangoproject.com/en/3.1/topics/db/models/#intermediary-manytomany
    wishlist = models.ForeignKey(
        Wishlist,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
        )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='wishlist_products'
        )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
        