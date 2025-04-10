# meals/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Meal
from .serializers import MealSerializer

@api_view(['GET', 'POST'])
def meal_list(request):
    if request.method == 'GET':
        meals = Meal.objects.all()

        # Filter meals by category (if provided)
        meal_filter = request.query_params.get('category', None)
        if meal_filter:
            meals = meals.filter(category=meal_filter)

        # Search meals by name (if provided)
        search_query = request.query_params.get('search', None)
        if search_query:
            meals = meals.filter(name__icontains=search_query)

        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
