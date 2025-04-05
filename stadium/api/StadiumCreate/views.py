from rest_framework import generics

from .serializers import StadiumCreateAPISerializer
from stadium.models import Stadium
from permissions.is_admin import IsAdmin


class StadiumCreateAPIView(generics.CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumCreateAPISerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return Stadium.objects.all().select_related('owner')
