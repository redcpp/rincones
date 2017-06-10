from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^buy/(?P<order_id>[\w-]+)/$', views.buy, name='buy'),
]
