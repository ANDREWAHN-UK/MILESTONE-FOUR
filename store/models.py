from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=50) 
    description = models.TextField() 
    is_active = models.BooleanField(default=True)     
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'categories' 
        ordering = ['-created_at'] 
        verbose_name_plural = 'Categories'  # otherwise the plural is categorys 

    def __str__(self):
        return self.name


class Product(models.Model): 
    """A class to define the products"""
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2
        ) 
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField() 
    description = models.TextField() 
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    #  ManyToMany means each product can be in several categories 
    categories = models.ManyToManyField(Category) 
 
    class Meta: 
        db_table = 'products' 
 
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Review(models.Model):
    """
    A model for users to create reviews
    """
    # This is used by the relevant form in forms.py
    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Product Reviews'

    rating_selection = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    product = models.ForeignKey(Product, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_selection, default=5)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title