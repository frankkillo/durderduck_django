from django.urls import path

from . import views


urlpatterns = [
    path('checkout-with-telegram/', views.checkout_with_telegram)
]