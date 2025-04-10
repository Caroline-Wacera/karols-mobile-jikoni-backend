# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list),  # Endpoint to list and create orders
    path('<int:order_id>/payment/', views.process_payment),  # Endpoint to process payments for an order
]
