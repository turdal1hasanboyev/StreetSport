from rest_framework.generics import ListAPIView
from .serializers import StadiumListUserAPISerializer
from apps.stadium.models import Stadium
from permissions.is_user import IsUser
from .filters import StadiumFilter


class StadiumListUserAPIView(ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumListUserAPISerializer
    permission_classes = [IsUser]
    filterset_class = StadiumFilter

    def get_queryset(self):
        return Stadium.objects.all().select_related('owner')
