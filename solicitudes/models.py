from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TipoPrueba(models.Model):
    tipo_prueba = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_prueba


class TipoEjecucion(models.Model):
    tipo_ejecucion = models.CharField(max_length=100)
    tipo_prueba = models.ForeignKey(TipoPrueba, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_ejecucion


class TipoAplicacion(models.Model):
    tipo_aplicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_aplicacion


class Ejecutor(models.Model):
    ejecutor = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.ejecutor + "-" + self.version


class Aplicacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_aplicacion = models.ForeignKey(TipoAplicacion, on_delete=models.CASCADE)
    link = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=100)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_aplicacion = models.ForeignKey(TipoAplicacion, on_delete=models.CASCADE)
    link = models.TextField(blank=True, null=True)
    ejecutor = models.ForeignKey(Ejecutor, on_delete=models.CASCADE, null=True)
    alto_pantalla = models.IntegerField(default=600)
    ancho_pantalla = models.IntegerField(default=800)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre + " " + self.ejecutor.__str__()


class Prueba(models.Model):
    nombre = models.CharField(max_length=100)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE, null=True)
    tipo_prueba = models.ForeignKey(TipoPrueba, on_delete=models.CASCADE)
    script = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    aplicacion = models.ManyToManyField(Aplicacion)
    herramienta = models.ManyToManyField(Herramienta)
    tipo_prueba = models.ManyToManyField(TipoPrueba)
    tipo_ejecucion = models.ManyToManyField(TipoEjecucion)
    pruebas = models.ManyToManyField(Prueba)
    descripcion = models.TextField(blank=True, null=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
