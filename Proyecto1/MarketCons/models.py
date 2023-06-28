from django.db import models

# Create your models here.

class Cliente(models.Model):
    usuario = models.CharField(max_length=20)
    contra = models.CharField(max_length=12)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Producto(models.Model):
    producto = models.CharField(max_length=30)
    precio = models.IntegerField()

class Centro_ayuda(models.Model):
    usuario = models.CharField(max_length=30)

class Empleado(models.Model):
    num_empleado = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()




