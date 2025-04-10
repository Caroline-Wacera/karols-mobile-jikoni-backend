# orders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list),
    path('<int:pk>/status/', views.update_order_status),
    path('<int:order_id>/payment/', views.process_payment),  # New endpoint for payment processing
]
