from rest_framework import serializers
from peak.models import Peak


class PeakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        fields = ('id', 'name', 'latitude', 'longitude', 'altitude')
