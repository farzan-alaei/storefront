from django.shortcuts import render
from django.db.models import Value, Func, F, Count, Max, Sum
from django.db.models.functions import Concat
from store.models import Product


def say_hello(request):
    queryset = Product.objects.annotate(
        total_sales=Sum('orderitem__quantity')
    ).order_by('-total_sales')[:5]

    return render(request, 'hello.html', {'name': 'Mosh', 'page_obj': queryset})
