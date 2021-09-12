"""
This model contains all the database design models for 'sonngs, 'albums' and 'playlists'.
"""

from django.db import models
from django.conf import settings
import datetime, os
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         related_name='album_artist'
    )
    audio_file = models.FileField()
    genre = models.CharField(max_length=255)
    year = models.IntegerField(
        default=current_year(),
        validators=[MinValueValidator(1984), max_value_current_year]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        blank=True
    )
    cover_image = models.FileField()

    
    def __str__(self):
        return f"{self.title} - {self.artist}"

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, 
    related_name='song_artist'
    )
    audio_file = models.FileField()
    album = models.ForeignKey(
        Album,
        on_delete=models.PROTECT,
        blank=True,
        null=True)
    genre = models.CharField(max_length=255)
    year = models.IntegerField(
        default=current_year(),
        validators=[MinValueValidator(1984), max_value_current_year]
    )
    uploaded_at = models.DateTimeField(default=timezone.now)
    duration = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        blank=True
        )
    cover_image = models.FileField()

   
    def __str__(self):
        return f"{self.title} - {self.artist}"

    