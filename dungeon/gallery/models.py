from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Artist(models.Model):
    id_artist = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

def year_choices():
    return [(r,r) for r in range(2018, datetime.date.today().year+1)]

#class MyForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)

class Song(models.Model):

    CHOICES_GENRE = (
    (0, "Trap"),
    (1, "R&B"),
    (2, "Cyber"),
    (3, "Reggaeton"),
    (4, "Drill"),
    (5, "Plugg"),
    (6, "Pluggnb"))
    
    id_song = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField()
    beat = models.BooleanField()
    mix = models.BooleanField()
    master = models.BooleanField()
    release_date = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year], choices=year_choices())
    genre = models.IntegerField(choices=CHOICES_GENRE)
    cover_art = models.ImageField(upload_to="coverart", null=True)
    id_artist = models.ForeignKey('Artist', models.DO_NOTHING)

    def __str__(self):
        return self.name + ' - ' + self.id_artist.name