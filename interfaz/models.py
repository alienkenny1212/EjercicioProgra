
from django.db import models
from django.conf import settings

#Create your models here.
class urla(models.Model):
    direccion = models.CharField(max_length=255)