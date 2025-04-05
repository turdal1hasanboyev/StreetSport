from rest_framework import serializers

from stadium.models import Stadium


class StadiumCreateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'
