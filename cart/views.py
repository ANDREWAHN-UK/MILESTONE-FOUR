from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from store.models import Category, Product 
from django.contrib import messages

# Create your views here.

def view_cart(request):
   
    return render(request, 'cart/cart.html')


# this view is based on the CI video Adding Products part1
# comments are mostly for me to get my head around how this works:
# this form is submitted to the view, including the item id and quantity
# then the cart variable is retrieved or created
# then the item is either updated or added
# then the variable cart is overwritten with the updated version of cart
# NB this gets called on the store page, though the view is in the cart app

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = Product.objects.get(pk=item_id)

    # quantity queries the form to determine what the user has entered
    # int turns it into a number
    quantity = int(request.POST.get('quantity', default=1))
    # below lets the form know where to send the user once form is submitted
    redirect_url = request.POST.get('redirect_url')
    
    cart = request.session.get('cart', {})
   
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name}  to your order')
    
    request.session['cart'] = cart
    
    return redirect(reverse('store'))

# More information on using sessions: https://docs.djangoproject.com/en/4.0/topics/http/sessions/

# this view is based on the CI video Adjusting and Removing Products part 1
def update_cart(request, item_id):
    """ update the cart with the adjusted number of items """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
   
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name}  from your order')
    
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))


# this view is based on the CI video Adjusting and Removing Products part 1
def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    
    cart.pop(item_id)
    messages.success(request, f'Removed {product.name}  from your order')

    request.session['cart'] = cart
    return HttpResponse(status=200)