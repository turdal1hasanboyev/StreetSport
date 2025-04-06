import django_filters
from stadium.models import Stadium


class StadiumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.RangeFilter()
    capacity = django_filters.RangeFilter()
    is_available = django_filters.BooleanFilter()

    class Meta:
        model = Stadium
        fields = ['name', 'location', 'price', 'capacity', 'is_available']
