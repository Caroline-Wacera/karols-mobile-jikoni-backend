# meals/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Meal  # Import the Meal model
from .serializers import MealSerializer  # Import the MealSerializer

# Create a view to handle the GET request for meals
class MealListView(APIView):
    def get(self, request):
        # Get all meal objects from the database
        meals = Meal.objects.all()
        
        # Serialize the data (convert to JSON format)
        serializer = MealSerializer(meals, many=True)
        
        # Return the serialized data in the response
        return Response(serializer.data)