from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Song


class SongListViewTest(APITestCase):
    def setUp(self):
        self.song1 = Song.objects.create(title='Song 1')
        self.song2 = Song.objects.create(title='Song 2')
        self.url = reverse('song_list')

    def test_song_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test
        self.assertEqual(len(response.data), 2)

        # test 2
        self.assertEqual(response.data[0]['title'], self.song1.title)
        self.assertEqual(response.data[1]['title'], self.song2.title)
