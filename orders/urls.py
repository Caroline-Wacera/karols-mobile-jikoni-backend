# orders/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list),
    path('<int:pk>/status/', views.update_order_status),
]
