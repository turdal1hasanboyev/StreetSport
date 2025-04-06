from rest_framework.views import APIView
from rest_framework.response import Response
from stadium.models import Stadium
from permissions.is_admin import IsAdmin


class StadiumCountAPIView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        count = Stadium.objects.count()
        
        return Response({'total_stadiums': count})
    