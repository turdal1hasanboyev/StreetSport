from rest_framework.serializers import ModelSerializer
from booking.models import Booking


class BookingCreateAPISerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']
