from rest_framework.generics import ListAPIView

from .serializers import StadiumListUserAPISerializer
from stadium.models import Stadium
from permissions.is_user import IsUser


class StadiumListUserAPIView(ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumListUserAPISerializer
    permission_classes = [IsUser]
    pagination_class = None

    def get_queryset(self):
        return Stadium.objects.all().select_related('owner')
