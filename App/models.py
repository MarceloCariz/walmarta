from django.db import models

# Create your models here.


class Nombre(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    grupo = models.CharField(max_length=15)
