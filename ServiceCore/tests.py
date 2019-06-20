from django.test import TestCase
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from .views import PostPreviewView

# Create your tests here.

# Klasa testowa dla URL widoku PostPreviewView
class PostPreviewViewTest(TestCase):
    def test_view_all_post_previews_unauthenticated(self):
        client = APIClient()
        response = client.get('/post_preview/')
        self.assertEqual(response.status_code, 200)


