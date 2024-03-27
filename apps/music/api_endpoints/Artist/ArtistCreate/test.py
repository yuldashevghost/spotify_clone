from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.music.models import Artist


class ArtistCreateViewTest(APITestCase):
    def setUp(self):
        pass

    def test_artist_create(self):
        url = reverse("album-create")
        data = {
            "id": "1",
            "avatar": open("media/avatar.jpeg", "rb"),
            "fullname": "test"

        }
        response = self.client.post(url, data)
        print(response.context)
        self.assertEqual(response.status_code, 201)


