# customers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.register_customer),
    path('customers/<int:pk>/', views.customer_profile),
]