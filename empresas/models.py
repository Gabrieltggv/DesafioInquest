from django.db import models


tipo = [
    ('PF', 'Pessoa física'),
    ('PF', 'Pessoa física'),
]


class Empresas(models.Model):
    razao_social = models.CharField(max_length=100, blank=False, null=False)
    cnpj = models.CharField(max_length=80, blank=False, null=False)
    dono = models.CharField(max_length=100, choices=tipo)

    class Meta:
        managed = True
        db_table = 'empresas'
        