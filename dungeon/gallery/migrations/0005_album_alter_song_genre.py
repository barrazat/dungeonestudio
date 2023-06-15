# Generated by Django 4.2.1 on 2023-06-15 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_song_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id_album', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('album_type', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.IntegerField(choices=[(0, 'Trap'), (1, 'R&B'), (2, 'Cyber'), (3, 'Reggaeton'), (4, 'Drill'), (5, 'Plugg'), (6, 'Pluggnb'), (7, 'Hard')]),
        ),
    ]
