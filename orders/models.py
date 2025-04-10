# orders/models.py

from django.db import models
from customers.models import Customer
from meals.models import Meal

class Order(models.Model):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    DELIVERED = 'Delivered'

    ORDER_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (DELIVERED, 'Delivered'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default=PENDING
    )
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"