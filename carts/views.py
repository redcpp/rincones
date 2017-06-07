from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart, CartItem


def view(request):
    try:
        the_id = request.session['cart_id']
    except Exception as e:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {'cart': cart}
    else:
        empty_message = 'Tu carrito está vacio, agrega algunas compras.'
        context = {'empty': True, 'empty_message': empty_message}

    template = 'cart/view.html'
    return render(request, template, context)

def update_cart(request, slug):
    request.session.set_expiry(120000)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except Exception as e:
        qty = None
        update_qty = False

    try:
        attr = request.GET.get('attr')
    except Exception as e:
        attr = None

    try:
        the_id = request.session['cart_id']
    except Exception as e:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Exception as e:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()

    '''if not cart_item in cart.items.all():
        cart.items.add(cart_item)
    else:
        cart.items.remove(cart_item)'''

    request.session['items_total'] = cart.cartitem_set.count()
    print(request.session['items_total'])
    cart.save()
    return redirect('carts:cart')
