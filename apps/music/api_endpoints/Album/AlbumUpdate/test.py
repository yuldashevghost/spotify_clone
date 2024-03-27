from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Album


class AlbumUpdateViewTest(APITestCase):
    def setUp(self):
        self.album = Album.objects.create(title='Initial Title', artist='Initial Artist')
        self.url = reverse('album_update', kwargs={'pk': self.album.pk})
        self.new_data = {'title': 'Updated Title', 'artist': 'Updated Artist'}

    def test_album_update(self):
        response = self.client.put(self.url, self.new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # next test -> albom malumotlari yangi ma'lumotlar bilan update boldi
        updated_album = Album.objects.get(pk=self.album.pk)
        self.assertEqual(updated_album.title, self.new_data['title'])
        self.assertEqual(updated_album.artist, self.new_data['artist'])
