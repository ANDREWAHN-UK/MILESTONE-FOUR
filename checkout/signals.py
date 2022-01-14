from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# the below is based on CI video Checkout -Part 3
# post means after here, not post as a verb


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()

    # More information on signals:
    # https://docs.djangoproject.com/en/4.0/topics/signals/

    