from django.db import models

class OrderStatus(models.Model):
    name = models.charField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    table_number = models.IntegerField(null=True, blank=True)
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.ForeignKey(
        orderStatus,
        on_delete=models.SET_NULL,
        null=True,
        related_name='orders'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"