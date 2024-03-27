from rest_framework.generics import ListAPIView

from apps.music.api_endpoints.Song.SongList.serializer import SongListSerializer
from apps.music.models import Song


class SongList(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongListSerializer

__all__ = ['SongList']