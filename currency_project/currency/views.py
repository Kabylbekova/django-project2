from django.shortcuts import render
from .models import Currency

def currency_list(request):
    currencies = Currency.objects.all()
    return render(request, 'currency_list.html', {'currencies': currencies})

