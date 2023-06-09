# Generated by Django 4.2 on 2023-04-30 15:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.base.servieces


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=160, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=src.base.servieces.path_to_artists_upload_image)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=160, unique=True)),
                ('comment', models.TextField()),
                ('ambiguity', models.FloatField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='The ambiguity of words')),
                ('slang', models.FloatField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='The complexity of slang')),
                ('speech_speed', models.FloatField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='The complexity of speech speed')),
                ('without_text', models.FloatField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='The complexity of the understanding without text')),
                ('data', models.DateField(default=datetime.date.today)),
                ('published', models.BooleanField(default=True)),
                ('artists', models.ManyToManyField(to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.date.today)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='music.music')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
