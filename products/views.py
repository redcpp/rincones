from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, ProductImage


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': products}
        template = 'products/results.html'
        return render(request, template, context)
    else:
        return redirect('/')


def home(request):
    featured = Product.objects.all()[:4]
    context = {'featured': featured}
    template = 'products/home.html'
    return render(request, template, context)

def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)

def single(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = ProductImage.objects.filter(product=product)
    context = {'product': product, 'images': images}
    template = 'products/single.html'
    return render(request, template, context)
