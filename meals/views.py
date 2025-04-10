from rest_framework import viewsets
from rest_framework import filters
from .models import Meal
from .serializers import MealSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    # Adding search and ordering functionality
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ['name', 'category']  # Allows search by name and category
    ordering_fields = ['name', 'price']  # Allows ordering by name or price
    ordering = ['name']  # Default ordering by name
