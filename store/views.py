from django.shortcuts import render, get_object_or_404, redirect, reverse
from store.models import Category, Product, Review
from .forms import ProductForm, ReviewForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)

from django.urls import reverse_lazy
# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'store/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Successfully added {product.name}!')
            return redirect(reverse('store'))
        else:
            messages.error(
                request, 'Failed to add product. Is the form valid?'
                )
    else:
        form = ProductForm()
     
    template = 'store/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('store'))
        else:
            messages.error(
                request, 'Failed to update product. Is the form valid?'
                )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'store/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} deleted!')
    return redirect(reverse('store'))


def review(request):
    """this is to display all reviews"""
    reviews = Review.objects.all()
    context = {'reviews': reviews}
    return render(request, 'store/reviews.html', context)


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'store/review_create.html'
    fields = (
        'title',
        'product',
        'image',
        'body',
        'rating',
        )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # nb, setting the form instance author above to self.request.user 
    # means the author is automatically the logged in user. 
    # For it to work, the author field must be removed from the fields settings

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'store/review_edit.html'
    fields = (
        'title',
        'product',
        'image',
        'body',
        'rating',
        )
    success_url = reverse_lazy('view_reviews')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'store/review_delete.html'
    success_url = reverse_lazy('store')
    