from django.contrib import admin
from .models import Usuario, Pelicula, Reseña

admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(Reseña)