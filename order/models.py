from django.db import models

from product.models import Product

class Order(models.Model):
    payload = models.PositiveBigIntegerField(default=0)
    costumer_id = models.CharField(max_length=52, blank=True, null=True)
    costumer_username = models.CharField(max_length=52, blank=True, null=True)
    first_name = models.CharField(max_length=52, blank=True, null=True)
    last_name = models.CharField(max_length=52, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country_code = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=52, blank=True, null=True)
    city = models.CharField(max_length=52, blank=True, null=True)
    street_line1 = models.CharField(max_length=52, blank=True, null=True)
    street_line2 = models.CharField(max_length=52, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    price_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_options_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)
    provider_payment_charge_id = models.CharField(max_length=52, blank=True, null=True)
    comment = models.CharField(max_length=152, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_at"]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)


