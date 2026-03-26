from django.test import TestCase
from .models import Order, OrderItem
from home.models import MenuItem
from decimal import Decimal

class OrderModelTest(TestCase):
    def test_calculate_total(self):
        # Create a dummy menu item and order
        burger = MenuItem.objects.create(name="Burger", price=10.00)
        order = Order.objects.create()

        # Add items to the order
        OrderItem.objects.create(order=order, menu_item=burger, quantity=2, price=10.00)
        OrderItem.objects.create(order=order, menu_item=burger, quantity=1, price=5.50)

        # Expected: (2 * 10.00) + (1 * 5.50) = 25.50
        self.assertEqual(order.calculate_total(), Decimal('25.50'))