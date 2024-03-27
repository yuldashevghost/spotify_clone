from rest_framework.generics import RetrieveAPIView

from apps.music.api_endpoints.Album.AlbumRetrieve.serializer import AlbumRetrieveSerializer
from apps.music.models import Album


class AlbumRetrieveView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumRetrieveSerializer

__all__ = ['AlbumRetrieveView']