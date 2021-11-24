from django.db.models.expressions import Value, F
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Customer


def say_hello(request):
    queryset = Customer.objects.annotate(is_new=Value(True))

    return render(request, 'hello.html', {'name': 'Amine', 'result': list(queryset)})
