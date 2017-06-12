from django.conf import settings
from django.conf import settings
from django.db import models
import os
import json

from carts.models import Cart


def convert_to_qr(self):
    return str(self)

def generate_json(self, facturas_path):
    json_name = f"{str(self)}.json"
    json_path = os.path.join(facturas_path, json_name)
    ngrok_image = f'http://fe303977.ngrok.io/media/facturas/{str(self)}.png'

    data = {}
    data['logo'] = ngrok_image
    data['from'] = 'ZetaSigma\nFacultad de Informática Juriquilla'
    data['to'] = f'{self.user.first_name} {self.user.last_name}'
    data['currency'] = 'mxn'
    data['number'] = str(self)
    data['payment_terms'] = '30 días para realizar el pago'
    data['notes'] = 'La reproducción apócrifa de este comprobante constituye un delito en los términos de las disposiciones fiscales.'
    data['terms'] = 'Esté comprobante tendrá una vigencia de dos años contados a partir de la fecha de aprobación de la asignación de folios.'
    for cart_item in self.cart.cartitem_set.all():
        item_data = {
            'name': str(cart_item),
            'quantity': str(cart_item.quantity),
            'unit_cost': str(cart_item.product.price)
            }
        data['items'] = data.get('items', []) + [item_data]

    with open(json_path, 'w') as fp:
        json.dump(data, fp, indent=4)

    return json_path


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    cart = models.ForeignKey(Cart)
    order_id = models.CharField(max_length=120, unique=True)
    finished = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    factura_url = models.CharField(max_length=600, null=True, blank=True)

    state = models.CharField(max_length=120, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    street = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    @property
    def total(self):
        return self.cart.total


    def get_factura_url(self):
        if not self.factura_url:
            facturas_path = os.path.join(settings.MEDIA_ROOT, 'facturas/')
            if not os.path.exists(facturas_path):
                os.makedirs(facturas_path)

            image_name = f"{str(self)}.png"
            image_path = os.path.join(facturas_path, image_name)
            qr_text = convert_to_qr(self)
            os.system( f"qrcode {qr_text} {image_path}" )

            pdf_name = f"{str(self)}.pdf"
            pdf_path = os.path.join(facturas_path, pdf_name)
            self.factura_url = f'/media//facturas/{pdf_name}'
            self.save()

            json_path = generate_json(self, facturas_path)

            os.system( f"node {settings.PDF_GENERATOR} {pdf_path} {json_path}" )


        return self.factura_url

    def __str__(self):
        return self.order_id

