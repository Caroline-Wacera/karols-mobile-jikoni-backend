from django.contrib import admin
from .models import Order, Meal

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'meal', 'quantity', 'status', 'order_date', 'delivery_date')
    search_fields = ('customer__name', 'meal__name')  # Ensure you're using correct fields
    list_filter = ('status', 'meal__category')  # Assuming `category` field exists in Meal model

# Registering the Meal model in the admin
admin.site.register(Meal)
