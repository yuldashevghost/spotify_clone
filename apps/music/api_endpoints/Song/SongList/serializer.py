from rest_framework import serializers

from apps.music.models import Song


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'cover', 'file', 'genres', 'album')