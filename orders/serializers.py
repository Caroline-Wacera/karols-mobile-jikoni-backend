# orders/serializers.py

from rest_framework import serializers
from .models import Order
from customers.models import Customer
from meals.models import Meal

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'meal', 'quantity', 'status', 'order_date', 'delivery_date']
