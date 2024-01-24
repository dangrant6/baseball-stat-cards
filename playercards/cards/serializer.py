from rest_framework import serializers
from .models import PositionPlayer, Pitcher

class PositionPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionPlayer
        fields = '__all__'

class PitcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitcher
        fields = '__all__'
