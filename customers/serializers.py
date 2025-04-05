# customers/serializers.py
from rest_framework import serializers
from .models import Customer  # Import the Customer model from the models file

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # This will include all fields from the Customer model in the serializer
