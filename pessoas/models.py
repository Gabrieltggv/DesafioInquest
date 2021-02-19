from django.db import models


class Pessoas(models.Model):
    cpf = models.CharField(max_length= 11, primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    rg = models.CharField(max_length=100, blank=False, null=False)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=80, blank=False, null=False)
    numero_endreco = models.IntegerField()
    bairro = models.CharField(max_length=60, blank=False, null=False)
    cep = models.CharField(max_length=100, blank=False, null=False)
    data_registro = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'pessoas'
