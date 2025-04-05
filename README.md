# Karol's Mobile Jikoni Backend

## Overview
Karol's Mobile Jikoni is an online platform for meal ordering and delivery. The backend API provides essential functionalities for managing meals, orders, customers, and payments.

## Features
- **Meal Management**: Add, update, delete, and retrieve meal details.
- **Order Management**: Place, update, and track orders.
- **Customer Management**: Register, update, and retrieve customer profiles.
- **Payment Integration**: Process payments for orders.

## API Endpoints
### Meal Endpoints
- `GET /api/meals/`: Retrieve all meals
- `POST /api/meals/`: Add a new meal
- `PUT /api/meals/{id}/`: Update meal details
- `DELETE /api/meals/{id}/`: Remove a meal from the catalog

### Order Endpoints
- `GET /api/orders/`: Retrieve all orders
- `POST /api/orders/`: Place a new order
- `PUT /api/orders/{id}/`: Update an order’s status

### Customer Endpoints
- `POST /api/customers/`: Register a new user
- `GET /api/customers/{id}/`: Retrieve customer profile

### Payment Endpoints
- `POST /api/orders/{order_id}/payment/`: Process payment for an order

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/karols-mobile-jikoni-backend.git