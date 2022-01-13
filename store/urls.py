from django.urls import path, include
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
        ),
    path('create/', views.create_review, name='create_review'),
    ]