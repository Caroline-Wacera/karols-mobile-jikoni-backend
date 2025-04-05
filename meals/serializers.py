# meals/serializers.py
from rest_framework import serializers
from .models import Meal  # Import the Meal model from the models file

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'  # This will include all fields from the Meal model in the serializer
