from rest_framework import generics

from stadium.models import StadiumManager
from permissions.is_owner import IsOwner
from .serializers import StadiumManagerCreateAPISerializer


class StadiumManagerCreateAPIView(generics.CreateAPIView):
    queryset = StadiumManager.objects.all()
    serializer_class = StadiumManagerCreateAPISerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return self.queryset.all().select_related('stadium', 'manager')
