# orders/admin.py

from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'meal', 'quantity', 'status', 'order_date', 'delivery_date')
    search_fields = ('customer__username', 'meal__name')
    list_filter = ('status', 'meal__category')
