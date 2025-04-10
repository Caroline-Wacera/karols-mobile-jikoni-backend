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
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        payment_method = request.data.get('payment_method')
        amount = order.meal.price * order.quantity  # Total amount for the order

        payment_data = {
            'order': order.id,
            'payment_method': payment_method,
            'amount': amount,
            'payment_status': 'Completed'  # Assume payment is successful for now
        }
        
        serializer = PaymentSerializer(data=payment_data)
        if serializer.is_valid():
            serializer.save()
            # Update the order's status to "Delivered" after payment
            order.status = 'Delivered'
            order.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)