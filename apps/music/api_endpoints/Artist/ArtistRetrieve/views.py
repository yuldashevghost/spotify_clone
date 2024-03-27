from rest_framework.generics import RetrieveAPIView

from apps.music.api_endpoints.Artist.ArtistRetrieve.serializer import ArtistRetrieveSerializer
from apps.music.models import Artist


class ArtistRetrieveView(RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistRetrieveSerializer

__all__ = ['ArtistRetrieveView']