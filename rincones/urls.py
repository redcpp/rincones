from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout, login
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('products.urls', namespace='products')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
