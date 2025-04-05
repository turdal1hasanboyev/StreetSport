from django.db import models


class Booking(models.Model):
    user = models.ForeignKey('user.CustomUser', related_name='booking_user', on_delete=models.CASCADE, limit_choices_to={'role': 'user'})
    stadium = models.ForeignKey('stadium.Stadium', related_name='booking_stadium', on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return f"Booking by {self.user.first_name} {self.user.last_name} at {self.stadium.name} from {self.start_time} to {self.end_time}"
