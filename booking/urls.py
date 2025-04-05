from django.urls import path

from .api.BookingCheckIn.views import CheckInAPIView


urlpatterns = [
    path('manager/check-in/<int:pk>/', CheckInAPIView.as_view(), name='manager-check-in'),
]
