from django.shortcuts import render
from store.models import Collection, Product


def say_hello(request):
    Collection.objects.filter(pk=11).delete()
    return render(request, 'hello.html', {'name': 'Mosh'})
