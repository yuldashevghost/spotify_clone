from rest_framework import serializers

from apps.music.models import Album


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'