from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Album


class AlbumRetrieveViewTest(APITestCase):
    def setUp(self):
        self.album = Album.objects.create(title='Test Album', artist='Test Artist')
        self.url = reverse('album_retrieve', kwargs={'pk': self.album.pk})

    def test_album_retrieve(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test2 ==> the retrieved data matches the album's data
        self.assertEqual(response.data['title'], self.album.title)
        self.assertEqual(response.data['artist'], self.album.artist)
