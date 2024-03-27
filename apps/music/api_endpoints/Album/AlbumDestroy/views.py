from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Album

class AlbumDestroyTest(APITestCase):
    def setUp(self):
        self.album = Album.objects.create(title='Test Album', artist='Test Artist')
        self.url = reverse('album_destroy', kwargs={'pk': self.album.pk})

    def test_album_destroy(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Album.objects.filter(pk=self.album.pk).exists())
