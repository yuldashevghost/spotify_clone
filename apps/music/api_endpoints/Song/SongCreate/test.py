from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Song

class SongCreateViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('song_create')
        self.valid_payload = {
            'title': 'Test Song',
            'cover': 'test_cover.jpeg',
            'file': 'test_song.mp3',
            'genres': ["jazz", "hiphop"],
            'album': "muhabbat",
            'listened': 0
        }

    def test_song_create(self):
        initial_count = Song.objects.count()
        response = self.client.post(self.url, self.valid_payload, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), initial_count + 1)
