from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Song


class SongUpdateViewTest(APITestCase):
    def setUp(self):
        self.song = Song.objects.create(title='Initial Title', listened=0)
        self.url = reverse('song_update', kwargs={'pk': self.song.pk})
        self.new_data = {'title': 'Updated Title', 'listened': 1}

    def test_song_update(self):
        response = self.client.put(self.url, self.new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test for the song instance is updated with new data
        updated_song = Song.objects.get(pk=self.song.pk)
        self.assertEqual(updated_song.title, self.new_data['title'])
        self.assertEqual(updated_song.listened, self.new_data['listened'])
