from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Song


class SongRetrieveViewTest(APITestCase):
    def setUp(self):
        self.song = Song.objects.create(title='Test Song', listened=0)
        self.url = reverse('song_retrieve', kwargs={'pk': self.song.pk})

    def test_song_retrieve(self):
        initial_listened_count = self.song.listened
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test for the song was retrieved successfully
        self.assertEqual(response.data['title'], self.song.title)

        # test for the 'listened' count has increased by 1
        updated_song = Song.objects.get(pk=self.song.pk)
        self.assertEqual(updated_song.listened, initial_listened_count + 1)
