from django.shortcuts import render
from django.db.models import Value
from store.models import Product


def say_hello(request):
    queryset = Product.objects.annotate(is_new=Value(True))

    return render(request, 'hello.html', {'name': 'Mosh', 'page_obj': queryset})
