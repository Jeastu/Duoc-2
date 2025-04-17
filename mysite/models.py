from django.db import models

# Create your models here.
class Construccion(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=200)  # usa CharField si son rutas estáticas
    materiales = models.TextField(help_text="Separados por comas")
    descripcion = models.TextField()

    def get_materiales_list(self):
        return [m.strip() for m in self.materiales.split(",")]

    def __str__(self):
        return self.nombre

      

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    hostilidad = models.CharField(max_length=100)  # ← corregido aquí
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Enemigo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Pueblo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class UbicacionEspecifica(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class UbicacionVariada(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
