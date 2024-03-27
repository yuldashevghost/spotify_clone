from rest_framework import serializers

from apps.music.models import Song


class SongUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'