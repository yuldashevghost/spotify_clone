# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Artist

class ArtistListTest(APITestCase):
    def setUp(self):
        Artist.objects.create(fullname='Artist 1', followers=100)
        Artist.objects.create(fullname='Artist 2', followers=200)

    def test_artist_list(self):
        url = reverse('artist_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
