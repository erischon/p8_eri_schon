from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class DatabaseTestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.credentials = {
            'username': 'admin',
            'password': 'secret',
            'is_staff': True,
        }
        User.objects.create_user(**self.credentials)

        self.user = User.objects.get(username='admin')

        self.etl_url = reverse('etl')


    def test_etl_view_not_logged(self):
        response = self.client.get(self.etl_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/database/')

    def test_etl_view_admin(self):
        self.client.login(**self.credentials)

        response = self.client.get(self.etl_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'database/etl.html')
