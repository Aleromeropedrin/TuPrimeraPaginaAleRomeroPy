from django import forms
from .models import Usuario, Pelicula, Reseña

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = "__all__"

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = "__all__"

class BuscarPeliculaForm(forms.Form):
    termino = forms.CharField(label="Buscar película", max_length=100)