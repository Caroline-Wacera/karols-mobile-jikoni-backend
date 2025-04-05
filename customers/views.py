# customers/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer  # Import the Customer model
from .serializers import CustomerSerializer  # Import the CustomerSerializer

# Create a view to handle the GET request for customers
class CustomerListView(APIView):
    def get(self, request):
        # Get all customer objects from the database
        customers = Customer.objects.all()
        
        # Serialize the data (convert to JSON format)
        serializer = CustomerSerializer(customers, many=True)
        
        # Return the serialized data in the response
        return Response(serializer.data)
