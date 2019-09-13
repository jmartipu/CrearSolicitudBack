from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    script = models.TextField()
    descripcion = models.TextField()
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
