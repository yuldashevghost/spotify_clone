from rest_framework import serializers

from apps.music.models import Artist


class ArtistUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'