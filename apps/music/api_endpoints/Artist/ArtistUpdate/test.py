from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Artist


class ArtistUpdateViewTest(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(fullname='Initial Name', followers=100)
        self.url = reverse('artist_update', kwargs={'pk': self.artist.pk})
        self.new_data = {'fullname': 'Updated Name', 'followers': 200}

    def test_artist_update(self):
        response = self.client.put(self.url, self.new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # test if the artist data is updated with new data
        updated_artist = Artist.objects.get(pk=self.artist.pk)
        self.assertEqual(updated_artist.fullname, self.new_data['fullname'])
        self.assertEqual(updated_artist.followers, self.new_data['followers'])
