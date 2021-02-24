from rest_framework import viewsets
from dono.models import Donos
from dono.api.serializers import DonosSerializer


class DonosViewSet(viewsets.ModelViewSet):
    queryset = Donos.objects.all()
    serializer_class = DonosSerializer