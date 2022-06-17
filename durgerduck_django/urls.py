from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from telegramevent import views as tgviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/products/', include('product.urls')),
    path('api/v1/orders/', include('order.urls')),
    path(f'{settings.TELEGRAM_TOKEN}/', tgviews.event_handler),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
