from rest_framework import viewsets
from empresas.models import Empresas
from empresas.api.serializers import EmpresasSerializer


class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    