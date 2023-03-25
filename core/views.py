from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Item
    template_name = "home-page.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"


def check_out(request):
    return render(request, "checkout-page.html")

