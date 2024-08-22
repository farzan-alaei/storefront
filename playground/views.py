from django.shortcuts import render
from django.db import connection
from store.models import Product


def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')

    # with connection.cursor() as cursor:
    #     cursor.callproc('get_customers', [1, 2, 'a'])

    return render(request, 'hello.html', {'name': 'Mosh', 'page_obj': queryset})
