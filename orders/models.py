from django.conf import settings
from django.db import models

from carts.models import Cart


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    cart = models.ForeignKey(Cart)
    order_id = models.CharField(max_length=120, unique=True)
    finished = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    state = models.CharField(max_length=120, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    street = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    @property
    def total(self):
        return self.cart.total

    def __str__(self):
        return self.order_id

