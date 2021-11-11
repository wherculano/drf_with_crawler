from django.db import models
from jsonfield import JSONField


class Notebook(models.Model):
    modelo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    hdd = JSONField()
    avaliacoes = models.IntegerField()
    nota = models.IntegerField()

    def __str__(self):
        return self.modelo
