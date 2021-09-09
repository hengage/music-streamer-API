"""
This model contains all the database design models for 'sonngs, 'albums' and 'playlists'.
"""

from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         related_name='artist'
    )
    album_file = models.FileField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='genre'
    )
    year = models.IntegerField(max_length=4)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.DecimalField(blank=True)
    cover_image = models.FileField()
    


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey('CustomUser', 
    on_delete=models.CASCADE, 
    related_name='artist'
    )
    song_file = models.FileField()
    genre = models.ForeignKey(Genre)
    year = models.IntegerField(max_length=4)
    duration = models.DecimalField(blank=True)
    cover_image = models.FileField()

    