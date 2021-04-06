from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from database.models import Product, Nutriscore
from search.views import saving, search_results

class UsersTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        nutriscore = Nutriscore.objects.create(nut_id=1, nut_type="C")
        self.product = Product.objects.create(
            prod_id = 3017620422003,
            prod_name = "test product",
            nut_id = nutriscore,
        )
        self.user = User.objects.create_user(
            username = "my username",
            password = "my pasword"
        )

        self.search_result_url = reverse('search_results')
        self.prodinfos_url = reverse('prodinfos', args=[self.product.prod_id])
        self.search_sub_url = reverse('search_sub')
        self.saving_url = reverse('saving', args=[self.product.prod_id])


    def test_signupuser_view(self):
        response = self.client.get(self.prodinfos_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/prodinfos.html')

    def test_loginuser_view(self):
        pass

    def test_moncompte_view(self):
        pass

    def test_myproducts_view(self):
        pass

    def test_myproducts_delete_view(self):
        pass