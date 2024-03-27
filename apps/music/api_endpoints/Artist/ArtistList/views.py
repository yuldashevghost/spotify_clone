from rest_framework.generics import ListAPIView

from apps.music.api_endpoints.Artist.ArtistList.serializer import ArtistListSerializer
from apps.music.models import Artist


class ArtistList(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer

__all__ = ['ArtistList']