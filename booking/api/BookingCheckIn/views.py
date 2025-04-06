from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from booking.models import Booking
from permissions.is_manager import IsManager


class CheckInAPIView(APIView):
    permission_classes = [IsManager]

    def post(self, request, pk):
        try:
            booking = Booking.objects.get(id=pk)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
        if booking.stadium.stadium_manager.manager != request.user:
            return Response({'error': 'You are not the manager of this stadium'}, status=status.HTTP_403_FORBIDDEN)
        booking.checked_in = True
        booking.save()
        return Response({'message': 'Booking checked in successfully'}, status=status.HTTP_200_OK)
