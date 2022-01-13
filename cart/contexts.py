from django.conf import settings
from django.shortcuts import get_object_or_404
from store.models import Product

def cart_contents(request):

    """returns the items in the cart"""

    cart_items = []
    total = 0
    product_count = 0
    delivery = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,        
        'grand_total': grand_total,
    }

    return context

    # This is a simplified version of the Code Institute contexts.py file, 
    # doing away with delivery as a variable of total spent,
    # as in this burger store, delivery would be handed off to Deliveroo et al,
    # and thus also with the need for decimal