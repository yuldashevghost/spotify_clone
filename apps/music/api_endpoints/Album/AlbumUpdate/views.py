from rest_framework.generics import UpdateAPIView

from apps.music.api_endpoints.Album.AlbumUpdate.serializer import AlbumUpdateSerializer
from apps.music.models import Album


class AlbumUpdateView(UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumUpdateSerializer

__all__ = ['AlbumUpdateView']