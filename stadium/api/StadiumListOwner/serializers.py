from rest_framework.serializers import ModelSerializer
from stadium.models import Stadium


class StadiumListOwnerAPISerializer(ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'
