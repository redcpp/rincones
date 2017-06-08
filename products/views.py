from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, ProductImage, Category


def home(request):
    destacados = Product.objects.all()[:6]
    recomendados = Product.objects.all()[:3]
    categories = Category.objects.all()
    context = {'destacados': destacados, 'recomendados': recomendados, 'categories': categories}
    template = 'products/home.html'
    return render(request, template, context)

def list(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    try:
        slug = request.GET.get('slug')
    except:
        slug = None

    if q:
        products = Product.objects.filter(title__icontains=q)
        location = q
    elif slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
        location = slug
    else:
        category = None
        products = Product.objects.all()
        location = 'Todo'

    categories = Category.objects.all()
    context = {'products': products, 'categories': categories, 'location': location}
    template = 'products/all.html'
    return render(request, template, context)

def single(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = ProductImage.objects.filter(product=product)
    recomendados = Product.objects.exclude(id=product.id)[:3]
    context = {'product': product, 'images': images, 'recomendados': recomendados}
    template = 'products/single.html'
    return render(request, template, context)
