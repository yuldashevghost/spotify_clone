from rest_framework import generics

from apps.music.api_endpoints.Song.SongCreate.serializer import SongCreateSerializer
from apps.music.models import Song


class SongCreateView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer

__all__ = ['SongCreateView']