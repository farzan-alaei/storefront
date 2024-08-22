from django.shortcuts import render
from django.db.models import Value, Func, F
from django.db.models.functions import Concat
from store.models import Customer


def say_hello(request):
    queryset = Customer.objects.annotate(full_name=Func(
        F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    
    query = Customer.objects.annotate(Concat=Concat('first_name', Value(' '), 'last_name'))

    return render(request, 'hello.html', {'name': 'Mosh', 'page_obj': query})
