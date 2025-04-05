from rest_framework import serializers

from payment.models import Payment


class AcceptPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
