# customers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer),
    path('profile/<int:pk>/', views.get_customer_profile),
]
