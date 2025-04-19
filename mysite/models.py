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

class Arma(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.numero} - {self.nombre}"


class Consumible(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=200)
    hambre_normal = models.IntegerField()
    agua_normal = models.IntegerField()
    vida_normal = models.IntegerField()
    energia_normal = models.IntegerField()
    hambre_dificil = models.IntegerField()
    agua_dificil = models.IntegerField()
    vida_dificil = models.IntegerField()
    energia_dificil = models.IntegerField()

    def __str__(self):
        return self.nombre


class Historia(models.Model):
    imagen = models.CharField(max_length=200, blank=True)
    texto = models.TextField(blank=True)

    def __str__(self):
        return f"Historia: {self.imagen or 'Texto narrativo'}"




from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

