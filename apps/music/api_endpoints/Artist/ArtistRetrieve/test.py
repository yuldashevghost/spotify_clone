# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Artist

class ArtistRetrieveViewTest(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(fullname='Test Artist', followers=100)
        self.url = reverse('artist_retrieve', kwargs={'pk': self.artist.pk})

    def test_artist_retrieve(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fullname'], self.artist.fullname)
        self.assertEqual(response.data['followers'], self.artist.followers)
