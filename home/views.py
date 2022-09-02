from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products':products,
    }
    
    return render(request, 'home.html')

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    
    context = {
        'products':products,
        'product_count':product_count,
    }
    
    return render(request, 'store.html', context)

def product_detail(request, id):
    single_product = Product.objects.get( id=id)
    context = {
        'single_product': single_product,
    }
    return render(request, 'product_detail.html', context)