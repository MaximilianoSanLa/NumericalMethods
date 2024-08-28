from django.db import models

class metodo(models.Model):
    x = models.CharField(max_length=255)
    y = models.CharField(max_length=255)