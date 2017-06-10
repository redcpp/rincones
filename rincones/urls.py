from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('products.urls', namespace='products')),
    url(r'', include('carts.urls', namespace='carts')),
    url(r'', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Epsilon Zeta'
