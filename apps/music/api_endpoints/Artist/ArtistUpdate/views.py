from rest_framework.generics import UpdateAPIView

from apps.music.api_endpoints.Artist.ArtistUpdate.serializer import ArtistUpdateSerializer
from apps.music.models import Artist


class ArtistUpdateView(UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistUpdateSerializer

__all__ = ['ArtistUpdateView']