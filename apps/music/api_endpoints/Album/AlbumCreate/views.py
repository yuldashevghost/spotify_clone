from rest_framework.generics import CreateAPIView

from apps.music.api_endpoints.Album.AlbumCreate.serializer import AlbumCreateSerializer
from apps.music.models import Album


class AlbumCreateView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer

__all__ = ['AlbumCreateView']