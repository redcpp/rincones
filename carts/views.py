from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def view(request):
    cart = Cart.objects.all()[0]
    context = {'cart': cart}
    template = 'cart/view.html'
    return render(request, template, context)

def update_cart(request, slug):
    cart = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except:
        return redirect('carts:cart')

    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)

    cart.total = sum(float(item.price) for item in cart.products.all())
    cart.save()
    return redirect('carts:cart')
