from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):
    template = 'products/home.html'
    featured = Product.objects.all()[:4]
    context = {'featured': featured}
    return render(request, template, context)

def all(request):
    template = 'products/all.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template, context)

def single(request, slug):
    template = 'products/single.html'
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, template, context)
