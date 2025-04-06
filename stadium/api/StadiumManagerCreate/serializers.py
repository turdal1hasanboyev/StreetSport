from rest_framework import serializers

from stadium.models import StadiumManager


class StadiumManagerCreateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumManager
        fields = '__all__'
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
