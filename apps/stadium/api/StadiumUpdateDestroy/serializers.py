from rest_framework.serializers import ModelSerializer
from apps.stadium.models import Stadium


class StadiumUpdateDestroyAPISerializer(ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
