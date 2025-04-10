# orders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.place_order),
    path('orders/<int:pk>/', views.update_order_status),
]
