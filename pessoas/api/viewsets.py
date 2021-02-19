from rest_framework import viewsets

from pessoas.models import Pessoas
from pessoas.api.serializers import PessoasSerializers


class PessoasViewset(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializers