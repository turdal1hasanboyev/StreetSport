from django.db import models
from django.utils import timezone


class PaymentManager(models.Manager):
    def accept_payment(self, payment_id):
        payment = self.get(id=payment_id)
        if payment.status != 'pending':
            raise ValueError("Payment is not pending")
        payment.status = 'completed'
        payment.updated_at = timezone.now()
        payment.save()
        return payment

    def failed_payment(self, payment_id):
        payment = self.get(id=payment_id)
        payment.status = 'failed'
        payment.updated_at = timezone.now()
        payment.save()
        return payment
    