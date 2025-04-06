from rest_framework.generics import ListAPIView
from .serializers import StadiumListOwnerAPISerializer
from stadium.models import Stadium
from permissions.is_owner import IsOwner
from .filters import StadiumFilter


class StadiumListOwnerAPIView(ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumListOwnerAPISerializer
    permission_classes = [IsOwner]
    filterset_class = StadiumFilter

    def get_queryset(self):
        return Stadium.objects.filter(owner=self.request.user).select_related('owner')
