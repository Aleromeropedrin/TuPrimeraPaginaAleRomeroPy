from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.PositiveIntegerField()
    sinopsis = models.TextField()

    def __str__(self):
        return f"{self.titulo} ({self.anio})"


class Reseña(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    comentario = models.TextField()
    puntaje = models.PositiveSmallIntegerField()  # Del 0 al 10
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.usuario} sobre {self.pelicula}"