# orders/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment, Order
from .serializers import PaymentSerializer

@api_view(['POST'])
def process_payment(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    # Simulate payment processing logic
    payment_data = {
        "order": order.id,
        "amount": order.meal.price * order.quantity,  # Simple calculation
        "payment_status": 'completed',  # In a real scenario, check payment gateway status
    }

    serializer = PaymentSerializer(data=payment_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
