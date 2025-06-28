from django.shortcuts import render, redirect
from .models import Pelicula, Reseña
from .forms import PeliculaForm, ReseñaForm, UsuarioForm, BuscarPeliculaForm
from django.db.models import Avg


def index(request):
    return render(request, "blog/index.html")


def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UsuarioForm()
    return render(request, "blog/usuario_form.html", {"form": form})


def crear_pelicula(request):
    if request.method == "POST":
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PeliculaForm()
    return render(request, "blog/pelicula_form.html", {"form": form})


def crear_reseña(request):
    if request.method == "POST":
        form = ReseñaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ReseñaForm()
    return render(request, "blog/reseña_form.html", {"form": form})


def buscar_pelicula(request):
    resultados = []
    if 'termino' in request.GET:
        form = BuscarPeliculaForm(request.GET)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            resultados = Pelicula.objects.filter(titulo__icontains=termino)
    else:
        form = BuscarPeliculaForm()
    return render(request, "blog/resultado_busqueda.html", {
        "form": form,
        "resultados": resultados
    })




def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    peliculas_con_promedio = []

    for p in peliculas:
        promedio = p.reseña_set.aggregate(Avg('puntaje'))['puntaje__avg']
        cantidad = p.reseña_set.count()
        peliculas_con_promedio.append({
            'titulo': p.titulo,
            'anio': p.anio,
            'promedio': round(promedio, 2) if promedio else 0,
            'cantidad': cantidad,
        })

    return render(request, "blog/listar_peliculas.html", {
        "peliculas": peliculas_con_promedio
    })