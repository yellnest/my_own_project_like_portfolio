from datetime import date

from django.contrib.auth.models import User
from django.db import models

from ..base.servieces import path_to_artists_upload_image


class Artist(models.Model):
    """Модель музыканта
    """
    nick = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)
    image = models.ImageField(upload_to=path_to_artists_upload_image, blank=True, null=True)

    def __str__(self):
        return self.nick


class Music(models.Model):
    """Модель песни
    """
    DIFFICULTIES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    song_title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)
    comment = models.TextField()
    ambiguity = models.FloatField(choices=DIFFICULTIES, verbose_name='The ambiguity of words')
    slang = models.FloatField(choices=DIFFICULTIES, verbose_name='The complexity of slang')
    speech_speed = models.FloatField(choices=DIFFICULTIES, verbose_name='The complexity of speech speed')
    without_text = models.FloatField(choices=DIFFICULTIES,
                                     verbose_name='The complexity of the understanding without text')
    data = models.DateField(default=date.today)
    published = models.BooleanField(default=True)
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.song_title


class Comment(models.Model):
    """Модель комментария
    """
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=date.today)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
