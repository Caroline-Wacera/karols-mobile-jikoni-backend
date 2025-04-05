# orders/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order  # Import the Order model
from .serializers import OrderSerializer  # Import the OrderSerializer

# Create a view to handle the GET request for orders
class OrderListView(APIView):
    def get(self, request):
        # Get all order objects from the database
        orders = Order.objects.all()
        
        # Serialize the data (convert to JSON format)
        serializer = OrderSerializer(orders, many=True)
        
        # Return the serialized data in the response
        return Response(serializer.data)