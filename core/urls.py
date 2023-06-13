from django.urls import path
from .views import (
    ItemDetailView,
    check_out,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('checkout/', check_out, name='check_out'),
    path('products/<slug>', ItemDetailView.as_view(), name='products'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove_from_cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]
