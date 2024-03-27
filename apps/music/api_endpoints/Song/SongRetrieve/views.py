from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView

from apps.music.api_endpoints.Song.SongRetrieve.serializer import SongRetrieveSerializer
from apps.music.models import Song


class SongRetrieveView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongRetrieveSerializer

    def get(self, request, *args, **kwargs):
        song = super().get(request, *args, **kwargs)
        song.listened += 1
        song.save()
        return song


__all__ = ['SongRetrieveView']
