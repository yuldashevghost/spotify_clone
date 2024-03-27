from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Song

class SongDeleteViewTest(APITestCase):
    def setUp(self):
        self.song = Song.objects.create(title='Test Song')
        self.url = reverse('song_delete', kwargs={'pk': self.song.pk})

    def test_song_delete(self):
        initial_count = Song.objects.count()
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Song.objects.count(), initial_count - 1)
        self.assertFalse(Song.objects.filter(pk=self.song.pk).exists())
