from unittest.mock import patch
from nose.tools import assert_true
import requests

from django.test import TestCase, Client
from django.urls import reverse

from database.extract import Extract
# from database.tests.off_data_test import off_result


class DatabaseTestClass(TestCase):

    # def setUp(self):
    #     self.extract = Extract()

    def test_request_response(self):
        response = requests.get('https://fr.openfoodfacts.org/cgi/search.pl')
        assert_true(response.ok)

    # @patch('database.extract.requests')
    # def test_extract(self, mock_requests):
    #     mock_requests.json = {'toto':'toto'}
    #     mock_requests.get = True

    #     response = self.extract.extract()
    #     print(response)
    #     self.assertEqual(
    #         response, 'ECHEC : les produits ne sont pas téléchargés.')
