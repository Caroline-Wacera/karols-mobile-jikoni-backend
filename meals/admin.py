# meals/admin.py

from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'ingredients')
    search_fields = ('name', 'category')
    list_filter = ('category',)
