from rest_framework.serializers import ModelSerializer

from booking.models import Booking


class BookingListAPISerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
