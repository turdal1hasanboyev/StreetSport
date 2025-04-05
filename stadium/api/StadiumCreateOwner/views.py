from rest_framework import generics

from .serializers import StadiumCreateOwnerAPISerializer
from stadium.models import Stadium
from permissions.is_owner import IsOwner


class StadiumCreateOwnerAPIView(generics.CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumCreateOwnerAPISerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Stadium.objects.all().select_related('owner')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
