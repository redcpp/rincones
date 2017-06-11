from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import time

from products.models import Category
from carts.models import Cart
from .models import Order

def history(request):
    orders = Order.objects.filter(user=request.user, finished=True)
    context = {'orders': orders}
    template = 'orders/history.html'
    return render(request, template, context)

@login_required
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except Exception as e:
        return redirect('carts:cart')

    try:
        new_order = Order.objects.get(cart=cart)
    except Exception as e:
        new_order = Order(user=request.user)
        new_order.cart = cart
        new_order.order_id = hash(str(new_order.user) + str(new_order.cart))
        new_order.save()

    context = {'order': new_order}
    template = 'orders/checkout.html'
    return render(request, template, context)

@login_required
def buy(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(order_id=order_id)
            order.state = request.POST['state']
            order.street = request.POST['street']
            order.postal_code = request.POST['postal-code']
            order.finished = True
            order.save()
            del request.session['cart_id']
            del request.session['items_total']
            return redirect('orders:history')
        except Exception as e:
            pass

    return redirect('orders:checkout')
