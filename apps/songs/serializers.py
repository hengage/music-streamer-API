from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Album, Song

class AlbumSerializer(serializers.ModelSerializer):
    model = Album
    fields = (
        'title', 'artist', 'audio_file',
         'genre', 'uploaded_at', 'year',
         'duration', 'cover_image',)

class SongSeriailizer(serializers.ModelSerializer):
    model = Song
    fields = (
        'title', 'artist', 'audio_file',
         'album', 'genre', 'uploaded_at',
          'year','duration', 'cover_image',
    )