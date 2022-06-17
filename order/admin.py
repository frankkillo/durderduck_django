from django.contrib import admin

from .models import Order, OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "price", "quantity"]


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "payload", "total_amount", "is_paid", "modified_at"]
    list_filter = ["is_paid", "created_at", "modified_at"]
    search_fields = ["costumer_username"]
    inlines = (OrderItemInline, )

admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
