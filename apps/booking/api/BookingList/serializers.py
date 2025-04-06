from rest_framework.serializers import ModelSerializer
from apps.booking.models import Booking


class BookingListAPISerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
