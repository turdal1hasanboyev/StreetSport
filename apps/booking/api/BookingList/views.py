from rest_framework.generics import ListAPIView
from .serializers import BookingListAPISerializer
from apps.booking.models import Booking
from permissions.is_owner import IsOwner
from .filters import BookingFilter


class BookingListAPIView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListAPISerializer
    permission_classes = [IsOwner]
    filterset_class = BookingFilter

    def get_queryset(self):
        return Booking.objects.all().select_related('user', 'stadium')
