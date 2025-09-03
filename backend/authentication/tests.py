from django.urls import reverse
from rest_framework.test import APITestCase

class UsersViewTests(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        return super().setUp()
        
    def test_get_users(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "List of users"})
        
    def test_post_user(self):
        response = self.client.post(self.register_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Create a new user"})