from django.shortcuts import render
from .models import Item


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)


def check_out(request):
    return render(request, "checkout-page.html")
