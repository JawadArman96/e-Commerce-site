from django.urls import path
from .views import item_list,check_out,products

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item_list'),
    path('checkout/', check_out, name='check_out'),
    path('products/', products, name='products')
]
