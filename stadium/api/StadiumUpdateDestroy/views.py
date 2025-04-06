from rest_framework.generics import UpdateAPIView, DestroyAPIView
from permissions.is_admin import IsAdmin
from .serializers import StadiumUpdateDestroyAPISerializer
from stadium.models import Stadium


class StadiumUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumUpdateDestroyAPISerializer
    permission_classes = [IsAdmin]
    lookup_field = 'pk'

    def  get_queryset(self):
        return self.queryset.all().select_related('owner')
