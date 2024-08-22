from django.shortcuts import render
from store.models import Collection, Product, Cart, CartItem


def say_hello(request):
    cart = Cart.objects.filter(pk=1).delete()

    return render(request, 'hello.html', {'name': 'Mosh'})
