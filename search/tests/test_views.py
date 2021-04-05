from django.test import TestCase, Client
from django.urls import reverse, resolve

from database.models import Product

class SearchTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        # self.product1 = Product.objects.get_or_create(prod_id=100)    
        self.prodinfos_url = reverse('prodinfos', args=[1])
        self.search_sub_url = reverse('search_sub')
        self.saving_url = reverse('saving', args=['8001505005592'])

    # def test_search_results(self):
    #     client = Client()

    #     response = client.get(reverse('search_results'))

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'search/results.html')

    # def test_prodinfos(self):

    #     response = self.client.get(self.prodinfos_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'search/prodinfos.html')

    def test_search_sub(self):

        response = self.client.get(self.search_sub_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'webapp/home.html')

    def test_saving(self):

        response = self.client.get(self.saving_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/myproducts.html')