from rest_framework import generics

from .models import Song, Album
from .serializers import AlbumSerializer, SongSeriailizer


class SongListAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSeriailizer