# orders/admin.py

from django.contrib import admin
from .models import Order, Payment
from meals.models import Meal
from customers.models import Customer

admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Meal)
admin.site.register(Customer)
