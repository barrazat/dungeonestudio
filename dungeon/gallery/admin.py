from django.contrib import admin
from .models import Artist, Song, Album, Tracklist

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Tracklist)