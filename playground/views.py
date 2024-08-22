from django.shortcuts import render
from django.db.models import Value, Func, F, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discounted_price=discounted_price)

    return render(request, 'hello.html', {'name': 'Mosh', 'page_obj': queryset})
