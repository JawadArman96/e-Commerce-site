from django import template
from core.models import OrderItem
from django.shortcuts import get_object_or_404

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        order_items = OrderItem.objects.filter(user=user)
        if order_items.exists():
            total_item = 0
            for order_item in order_items:
                total_item = total_item + order_item.quantity
            return total_item
    return 0
