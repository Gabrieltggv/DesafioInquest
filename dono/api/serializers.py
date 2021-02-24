from rest_framework import serializers
from dono.models import Donos

class DonosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donos
        fields = '__all__'