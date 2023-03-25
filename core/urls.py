from django.urls import path
from .views import ItemDetailView, check_out, HomeView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('checkout/', check_out, name='check_out'),
    path('products/<slug>', ItemDetailView.as_view(), name='products')
]
