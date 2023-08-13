from django.shortcuts import render
from django.http import JsonResponse
from app.models import Product

def products(request):
    products = Product.objects.all().values()
    return JsonResponse({'products': list(products)})

def home(request):
    return HttpResponse("This is the home page")