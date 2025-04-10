from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealViewSet

# Create a router and register the MealViewSet with it
router = DefaultRouter()
router.register(r'meals', MealViewSet)

# Include the router-generated URLs in the urlpatterns list
urlpatterns = [
    path('', include(router.urls)),
]
