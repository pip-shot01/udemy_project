from django.shortcuts import render, redirect

# Create your views here.

def car(request):
    return render(request, 'cart.html')