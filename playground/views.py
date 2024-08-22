from django.shortcuts import render
from django.db.models.aggregates import Count, Sum, Min, Max, Avg
from store.models import Order, Collection, Product


def say_hello(request):
    collection_3 = Collection.objects.get(
        pk=3)  # Assuming collection 3 has ID 3
    min_price = Product.objects.filter(collection=collection_3).aggregate(
        Min('unit_price'))['unit_price__min']
    max_price = Product.objects.filter(collection=collection_3).aggregate(
        Max('unit_price'))['unit_price__max']
    avg_price = Product.objects.filter(collection=collection_3).aggregate(
        Avg('unit_price'))['unit_price__avg']
    return render(request, 'hello.html', {'name': 'Mosh', 'min': min_price, 'max': max_price, 'avg': avg_price})
