# orders/serializers.py
from rest_framework import serializers
from .models import Order  # Import the Order model from the models file

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # This will include all fields from the Order model in the serializer
