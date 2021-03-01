from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from webapp.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_hp_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_hp_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>The Substitute</title>', html)
        self.assertTrue(html.endswith('</html>'))