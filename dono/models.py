from django.db import models
from empresas.models import Empresas

class Donos(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=100, blank=False, null=False)
    empresa = models.ManyToManyField(Empresas)

    class Meta:
        managed = True
        db_table = 'dono'

    def __str__(self):
        return '%s' % (self.title)
        