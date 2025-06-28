# TuPrimeraPaginaAleRomero

Este es un proyecto realizado en Django siguiendo indicaciones de las clases.  
Es una web estilo blog dedicada a reseñas de películas.

---

## 🎯 Funcionalidades principales

- Registro de usuarios, películas y reseñas.
- Formularios para crear datos de cada modelo.
- Búsqueda de películas por título.
- Ranking de películas basado en puntaje promedio.
- Herencia de plantillas HTML.
- Estilizado con Bootstrap y Font Awesome.


---

## 🧱 Modelos

### Usuario
- nombre
- email (único)

### Pelicula
- titulo
- anio
- sinopsis

### Reseña
- usuario (ForeignKey)
- pelicula (ForeignKey)
- comentario
- puntaje (1 al 10)

---

## 📦 Requisitos

- Python 3.10+
- Django 4.x

---
