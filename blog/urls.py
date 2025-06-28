from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crear-usuario/", views.crear_usuario, name="crear_usuario"),
    path("crear-pelicula/", views.crear_pelicula, name="crear_pelicula"),
    path("crear-reseña/", views.crear_reseña, name="crear_reseña"),
    path("buscar-pelicula/", views.buscar_pelicula, name="buscar_pelicula"),
    path("listar-peliculas/", views.listar_peliculas, name="listar_peliculas"),
]