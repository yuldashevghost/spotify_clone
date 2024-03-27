from rest_framework import serializers

from apps.music.models import Album


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'