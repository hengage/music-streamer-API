from rest_framework import generics

from .models import Song, Album
from .serializers import AlbumSerializer, SongSeriailizer


class SongListAPIView(generics.ListAPIView):
    serializer_class = SongSeriailizer
    queryset = Song.objects.all()

class SongDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SongSeriailizer
    queryset = Song.objects.all()
    lookup_field = 'slug'