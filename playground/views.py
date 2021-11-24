from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Collection, Product


def say_hello(request):
    result = Product.objects.filter(collection__id=1).aggregate(
        count=Count('id'), min_price=Min('unit_price'))

    return render(request, 'hello.html', {'name': 'Amine', 'result': result})
