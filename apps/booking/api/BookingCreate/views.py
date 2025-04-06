from rest_framework.generics import CreateAPIView
from .serializers import BookingCreateAPISerializer
from apps.booking.models import Booking
from permissions.is_user import IsUser


class BookingCreateAPIView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateAPISerializer
    permission_classes = [IsUser]

    def get_queryset(self):
        return Booking.objects.all().select_related('user', 'stadium')
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
