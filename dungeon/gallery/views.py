from django.shortcuts import render
from .models import Artist, Song, Album, Tracklist
# Create your views here.
def home(request):
    songs = Song.objects.all()
    tracklist = Tracklist.objects.all()
    data = {
        'songs' : songs,
        'tracklist': tracklist
    }
    return render(request, 'home.html', data)
