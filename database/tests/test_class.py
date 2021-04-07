from unittest.mock import MagicMock

from django.test import SimpleTestCase

from .off_data_test import off_result
from database.extract import Extract

class MockRequestGet:
    def __init__(self, url, params=None, headers=None):
        pass 
    def json(self):
        return off_result

class DatabaseTestClass(SimpleTestCase):

    def setUp(self):
        extract = Extract()

    def test_extract(self):
        response = extract.extract()

        self.assertEqual(response, 1)