from django.shortcuts import render
from .models import Artist, Song
# Create your views here.
def home(request):
    songs = Song.objects.all()
    data = {
        'songs' : songs
    }
    return render(request, 'home.html', data)
