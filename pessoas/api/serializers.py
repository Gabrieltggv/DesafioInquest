from rest_framework import serializers
from pessoas.models import Pessoas


class PessoasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = '__all__'