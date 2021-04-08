from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from database.extract import Extract
# from database.tests.off_data_test import off_result

class DatabaseTestClass(TestCase):

    def setUp(self):
        self.extract = Extract()

    @patch('database.extract.requests')
    def test_extract(self, mock_requests):
        mock_requests.json = 1
        mock_requests.get = 1

        response = self.extract.extract()

        self.assertEqual(response, 'ECHEC : les produits ne sont pas téléchargés.')

    