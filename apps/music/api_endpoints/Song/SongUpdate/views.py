from rest_framework.generics import UpdateAPIView

from apps.music.api_endpoints.Song.SongUpdate.serializer import SongUpdateSerializer
from apps.music.models import Song


class SongUpdateView(UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongUpdateSerializer

__all__ = ['SongUpdateView']