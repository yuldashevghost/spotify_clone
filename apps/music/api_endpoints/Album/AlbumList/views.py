from rest_framework.generics import ListAPIView

from apps.music.api_endpoints.Album.AlbumList.serializer import AlbumListSerializer
from apps.music.models import Album


class AlbumListView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumListSerializer

__all__ = ['AlbumListView']