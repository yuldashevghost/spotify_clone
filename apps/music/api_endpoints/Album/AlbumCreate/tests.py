import json

from django.core.files import File
from django.urls import reverse
from rest_framework.test import APITestCase



class AlbumCreateTest(APITestCase):
    def setUp(self):
        pass
    def test_album_create(self):
        url = reverse("album-create")
        data = {
            "tile": "test",
            "author": "test",
            "cover": open("media/cover.jpeg", "rb")
        }
        response = self.client.post(url, data)
        print(response.context)
        self.assertEqual(response.status_code, 201)
