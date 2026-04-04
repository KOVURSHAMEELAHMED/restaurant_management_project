class Reservation(models.Model):
    # Example fields
    customer_name = models.CharField(max_length=100)
    reservation_datetime = models.DateTimeField()
    party_size = models.PositiveIntegerField()

    # Assign the custom manager
    objects = ReservationManager()

    def __str__(self):
        return f"{self.customer_name} - {self.reservation_datetime}"