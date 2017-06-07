from django.db import models

from products.models import Product

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    @property
    def total_cost(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.title

class Cart(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    @property
    def total(self):
        return sum(item.total_cost for item in self.cartitem_set.all())

    def __str__(self):
        return 'Cart id: {}'.format(self.id)

