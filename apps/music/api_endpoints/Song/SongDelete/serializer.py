from rest_framework import serializers

from apps.music.models import Song


class SongDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'