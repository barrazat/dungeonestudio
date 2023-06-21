from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from gallery import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cancion/crear/', views.create_song, name ='create-song'),
    path('album/crear/', views.create_album, name = 'create-album'),
    path('tracklist/crear/',views.create_tracklist, name = 'create-tracklist')
]