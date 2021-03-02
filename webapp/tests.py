from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_hp_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'webapp/home.html')