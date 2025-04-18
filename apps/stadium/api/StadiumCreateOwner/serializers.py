from rest_framework import serializers
from apps.stadium.models import Stadium


class StadiumCreateOwnerAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']
