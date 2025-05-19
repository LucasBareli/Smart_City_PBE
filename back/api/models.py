from django.db import models

class Sensores(models.Model):
    sensor = models.CharField(max_length=100)
    mac_adress = models.CharField(max_length=256)
    unidade_med = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.BooleanField()

class Ambientes(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=256)
    ni = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)

class Historicos(models.Model):
    sensor = models.ForeignKey('Sensores', on_delete=models.CASCADE)
    ambiente = models.ForeignKey('Ambientes', on_delete=models.CASCADE)
    Valor = models.FloatField()
    timestamp = models.IntegerField()