from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_lenght=64)
    comision= models.IntegerField()


class Estudiante(models.Model):
    nombre= models.CharField(max_length=256)
    apellido= models.CharField(max_length=256)
    email=models.EmailField(blank=True)
    telefono=models.CharField(max_length=50,blank=True)
    dni=models.CharField(max_length=32)
    fecha_nacimiento=models.DateField(null=True)

class Profesor(models.Model):
    nombre= models.CharField(max_length=256)
    apellido= models.CharField(max_length=256)
    email=models.EmailField(blank=True)
    telefono=models.CharField(max_length=50,blank=True)
    dni=models.CharField(max_length=32)
    fecha_nacimiento=models.DateField(null=True)
    profesion=models.CharField(max_length=256)
    bio=models.TextField(blank=True)

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False) 

