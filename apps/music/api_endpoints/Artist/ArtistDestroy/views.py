from rest_framework.generics import DestroyAPIView

from apps.music.api_endpoints.Artist.ArtistDestroy.serializer import ArtistDeleteSerializer
from apps.music.models import Artist


class ArtistDeleteView(DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDeleteSerializer

__all__ = ['ArtistDeleteView']