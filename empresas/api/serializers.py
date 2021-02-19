from rest_framework import serializers
from empresas.models import Empresas

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fildes = '__all__'