# orders/urls.py
from django.urls import path
from .views import OrderListView  # Import the OrderListView from views

# Define the URL patterns for the orders app
urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),  # Use '' since 'orders/' is defined in the main urls.py
]
