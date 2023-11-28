from django.db import models

# Create your models here.
class Reservas(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=11)
    fechaReserva = models.DateField(auto_now=False)
    horaReserva = models.TimeField(auto_now=False)
    cantidadClientes = models.CharField(max_length=3)
    email = models.EmailField(max_length=60, default="")
    estadoReserva = models.CharField(max_length=20)
    observacion = models.TextField(blank=True,null=True)