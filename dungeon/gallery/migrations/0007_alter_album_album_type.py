# Generated by Django 4.2.1 on 2023-06-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_tracklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_type',
            field=models.IntegerField(choices=[(0, 'EP'), (1, 'Álbum'), (2, 'LP')]),
        ),
    ]
