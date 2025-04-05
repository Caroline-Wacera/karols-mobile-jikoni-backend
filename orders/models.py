from django.db import models
from customers.models import Customer
from meals.models import Meal

class Order(models.Model):
    # Foreign Key to Customer (each order belongs to a customer)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    
    # Foreign Key to Meal (each order has one meal)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    
    # Quantity of the meal ordered
    quantity = models.IntegerField()
    
    # Status of the order (Pending, In Progress, Delivered)
    status = models.CharField(max_length=20, default='Pending')
    
    # Order and delivery timestamps
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Order {self.id} for {self.customer.username} - {self.status}"

