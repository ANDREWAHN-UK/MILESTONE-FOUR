from django.contrib import admin
from store.models import Product, Category, Review
from store.forms import ProductAdminForm, ReviewForm

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    # sets values for how the admin site lists your products 
    list_display = ('name', 'price',)
    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    
    search_fields = [
        'name',
        'description',
        ]
    exclude = ('created_at', 'updated_at',)
     

class CategoryAdmin(admin.ModelAdmin):
    # sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description',]
    exclude = ('created_at', 'updated_at',)


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    # sets values for how the admin site lists your products 
    list_display = ('name', 'price',)
    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    
    search_fields = [
        'name',
        'description',
        'title',
        'rating',        
        ]
    exclude = ('created_at', 'updated_at',)