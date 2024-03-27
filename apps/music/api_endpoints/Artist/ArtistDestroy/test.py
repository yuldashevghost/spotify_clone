# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.music.models import Artist


class ArtistDeleteViewTest(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(fullname='Test Artist', followers=100)
        self.url = reverse('artist_delete', kwargs={'pk': self.artist.pk})

    def test_artist_delete(self):
        initial_count = Artist.objects.count()
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artist.objects.count(), initial_count - 1)
        self.assertFalse(Artist.objects.filter(pk=self.artist.pk).exists())
