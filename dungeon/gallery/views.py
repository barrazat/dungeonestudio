from django.shortcuts import render
from .models import Artist, Song, Album, Tracklist
from .forms import ArtistForm, SongForm, AlbumForm, TracklistForm
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

def home(request):
    songs = Song.objects.all()
    tracklist = Tracklist.objects.all()
    data = {
        'songs' : songs,
        'tracklist': tracklist
    }
    return render(request, 'home.html', data)

@permission_required('dungeon.add_song')
def create_song(request):
    data = {
        'form': SongForm()
    }

    if request.method == 'POST':
        formulario = SongForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Canción guardada con exito.")
        else:
            data["form"] = formulario       
    return render(request, 'song/create.html', data)

@permission_required('dungeon.add_album')
def create_album(request):
    data = {
        'form': AlbumForm()
    }

    if request.method == 'POST':
        formulario = AlbumForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Álbum guardado con exito.")
        else:
            data["form"] = formulario       
    return render(request, 'song/create.html', data)

@permission_required('dungeon.add_tracklist')
def create_tracklist(request):
    data = {
        'form': TracklistForm()
    }

    if request.method == 'POST':
        formulario = TracklistForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tracklist guardado con exito.")
        else:
            data["form"] = formulario       
    return render(request, 'song/create.html', data)