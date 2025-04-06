from rest_framework.serializers import ModelSerializer
from apps.stadium.models import Stadium


class StadiumListOwnerAPISerializer(ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'
