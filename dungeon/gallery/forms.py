from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission, User, Group
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import DateTimeInput
from datetime import date
from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'