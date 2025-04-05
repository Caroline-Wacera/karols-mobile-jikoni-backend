# meals/urls.py
from django.urls import path
from .views import MealListView  # Import your view

urlpatterns = [
    path('', MealListView.as_view(), name='meal-list'),
]