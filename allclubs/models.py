from django.db import models

# Create your models here.

class Clubs(models.Model):
    nombre = models.CharField(max_length=50)
    sede = models.CharField(max_length=50)
    numero_club = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Entrenadores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Deportistas(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    posicion = models.CharField(max_length=30)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre
    
class Equipamiento(models.Model):
    articulo = models.CharField(max_length=30)
    serie = models.IntegerField()
    sede = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    usando = models.BooleanField()

    def __str__(self):
        return self.articulo