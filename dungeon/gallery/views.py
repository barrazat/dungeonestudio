from django.shortcuts import render
from .models import Artist, Song, Album, Tracklist
from .forms import ArtistForm, SongForm, AlbumForm, TracklistForm
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http.response import Http404

def home(request):
    songs = Song.objects.all()
    tracklist = Tracklist.objects.all()
    data = {
        'songs' : songs,
        'tracklist': tracklist
    }
    return render(request, 'home.html', data)

@permission_required('dungeon.add_artist')
def create_artist(request):
    data = {
        'form': ArtistForm()
    }

    if request.method == 'POST':
        formulario = ArtistForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Artista guardado con éxito.")
        else:
            data["form"] = formulario       
    return render(request, 'artist/create.html', data)

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
    return render(request, 'album/create.html', data)

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
    return render(request, 'tracklist/create.html', data)

def read_artist(request):
    artists = Artist.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(artists, 5)
        artists = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':artists,
        'paginator':paginator
    }
    return render(request, 'artist/read.html',data)

def read_song(request):
    songs = Song.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(songs, 5)
        songs = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':songs,
        'paginator':paginator
    }
    return render(request, 'song/read.html',data)