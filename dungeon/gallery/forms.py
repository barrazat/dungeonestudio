from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User, Group
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import DateTimeInput
from datetime import date
from .models import Artist, Song, Tracklist, Album

class ArtistForm(forms.ModelForm):
    name = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Artista'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url de Spotify, YouTube, etc.'}))
    class Meta:
        model = Artist
        fields = ['name', 'url']

class SongForm(forms.ModelForm):
    CHOICES_GENRE = (
        (0, "Trap"),
        (1, "R&B"),
        (2, "Cyber"),
        (3, "Reggaeton"),
        (4, "Drill"),
        (5, "Plugg"),
        (6, "Pluggnb"),
        (7, "Hard")
    )

    name = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Canción'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url de Spotify, YouTube, etc.'}))
    genre = forms.ChoiceField(choices=CHOICES_GENRE)
    class Meta:
        model = Song
        fields = ['name', 'url', 'beat', 'mix', 'master', 'release_date', 'genre', 'cover_art', 'id_artist']