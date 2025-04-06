import django_filters
from booking.models import Booking


class BookingFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFromToRangeFilter()
    end_time = django_filters.DateTimeFromToRangeFilter()
    status = django_filters.CharFilter(lookup_expr='iexact')
    checked_in = django_filters.BooleanFilter()
    stadium = django_filters.NumberFilter(field_name='stadium__id')
    user = django_filters.NumberFilter(field_name='user__id')

    class Meta:
        model = Booking
        fields = ['start_time', 'end_time', 'status', 'checked_in', 'stadium', 'user']
