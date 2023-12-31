# Generated by Django 4.2.1 on 2023-06-15 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_album_alter_song_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracklist',
            fields=[
                ('id_tracklist', models.AutoField(primary_key=True, serialize=False)),
                ('id_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.album')),
                ('id_song', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gallery.song')),
            ],
        ),
    ]
