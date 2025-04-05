# customers/urls.py
from django.urls import path
from .views import CustomerListView  # Import your view

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
]