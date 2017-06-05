from django.shortcuts import render

from .models import Cart


def view(request):
    cart = Cart.objects.all()[0]
    context = {'cart': cart}
    template = 'cart/view.html'
    return render(request, template, context)
