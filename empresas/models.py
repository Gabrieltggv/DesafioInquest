from django.db import models


class Empresas(models.Model):
    razao_social = models.CharField(max_length=100, blank=False, null=False)
    cnpj = models.CharField(max_length=80, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'empresas'
        
    def __str__(self):
        return self.razao_social
        