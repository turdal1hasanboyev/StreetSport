from django.urls import path

from .api.BookingCheckIn.views import CheckInAPIView
from .api.BookingList.views import BookingListAPIView


urlpatterns = [
    path('manager/check-in/<int:pk>/', CheckInAPIView.as_view(), name='manager-check-in'),
    path('booking-list/', BookingListAPIView.as_view(), name='booking-list'),
]
