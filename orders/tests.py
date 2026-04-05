from django.test import TestCase
from .models import Order

class OrderRevenueTest(TestCase):
    def setUp(self):
        # Create completed orders
        Order.objects.create(total_amount=100.00, status='COMPLETED')
        Order.objects.create(total_amount=50.00, status='COMPLETED')
        # Create a pending order (should be ignored)
        Order.objects.create(total_amount=75.00, status='PENDING')

    def test_calculate_total_revenue(self):
        total = Order.calculate_total_revenue()
        self.assertEqual(total, 150.00)