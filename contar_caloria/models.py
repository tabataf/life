from django.db import models
from django.forms import CharField

# Create your models here.

class Calorias (models.Model):
    nome_refeicao = models.CharField(max_length=40)
    alimento = models.CharField(max_length=100)
    qt_calorias = models.DecimalField(max_digits=15, decimal_places=5)

class TipoRefeicao(models.Model):

    tipo_refeicao= models.CharField(max_length=1, blank=False, null=False)
    nome_refeicao = models.TextField(max_length=16, null=False, blank=False)

    def __str__(self):
        return self.nome_refeicao
