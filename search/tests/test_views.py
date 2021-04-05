from django.test import TestCase, Client
from django.urls import reverse
from database.models import Product, Prodcat, Categorie, User

class SearchTestViews(TestCase):

    def test_search_results(self):
        client = Client()

        response = client.get(reverse('search_results', args=['some-product']))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/results.html')


