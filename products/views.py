from django.shortcuts import render

from .models import Product


def home(request):
    username_is = 'Juan' if request.user.is_authenticated() else 'Anon'
    context = {'username_is': username_is}
    template = 'products/home.html'
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template ='products/all.html'
    return render(request, template, context)
