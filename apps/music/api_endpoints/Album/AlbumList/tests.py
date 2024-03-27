from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Album


class AlbumListTest(APITestCase):
    def setUp(self):
        self.album1 = Album.objects.create(title='Album 1', artist='Artist 1')
        self.album2 = Album.objects.create(title='Album 2', artist='Artist 2')
        self.url = reverse('album_list')

    def test_album_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test for both albums are present in the response
        self.assertEqual(len(response.data), 2)

        # test for the response data matches the albums data
        self.assertEqual(response.data[0]['title'], self.album1.title)
        self.assertEqual(response.data[0]['artist'], self.album1.artist)
        self.assertEqual(response.data[1]['title'], self.album2.title)
        self.assertEqual(response.data[1]['artist'], self.album2.artist)
