from django.db import models

class Clase1(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.TextField()

class Clase2(models.Model):
    campo3 = models.IntegerField()
    campo4 = models.DateField()

class Clase3(models.Model):
    campo5 = models.BooleanField(default=False)
    campo6 = models.DecimalField(max_digits=5, decimal_places=2)
