from django.db import models

from .managers import PaymentManager


class Payment(models.Model):
    booking = models.OneToOneField('booking.Booking', related_name='payment_booking', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('credit', 'Credit Card'), ('paypal', 'PayPal')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PaymentManager()

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f"Payment for {self.booking.user.first_name} {self.booking.user.last_name} - Amount: {self.amount}"
