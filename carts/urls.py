from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart/$', views.view, name='cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', views.update_cart, name='update_cart'),
]
