from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from gallery import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cancion/agregar/', views.create_song, name='create-song')
    #path('artist/', views.artist, name="artist")
]