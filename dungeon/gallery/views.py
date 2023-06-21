from django.shortcuts import render
from .models import Artist, Song, Album, Tracklist
from .forms import ArtistForm, SongForm
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

@permission_required('app.add_producto')
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