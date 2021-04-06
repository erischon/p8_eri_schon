from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User, AnonymousUser

from database.models import Product, Nutriscore

class UsersTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        self.user = User.objects.create_user(**self.credentials)

        self.signupuser_url = reverse('signupuser')
        self.moncompte_url = reverse('moncompte')
        self.myproducts_url = reverse('myproducts')
        self.myproducts_delete_url = reverse('myproducts_delete', args=['1'])


    def test_signupuser_view(self):
        response = self.client.get(self.signupuser_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')


    ### Method loginuser ###
    def test_loginuser_view(self):
        response = self.client.post('/users/login/', self.credentials, follow= True )

        self.assertTrue(response.context['user'].is_active)
        self.assertEquals(response.status_code, 200)

    def test_loginuser_view_user_is_none(self):
        response = self.client.post('/users/login/', {'username': 'none', 'password': 'none'} )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_loginuser_view_get_method(self):
        response = self.client.get('/users/login/')

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


    def test_logoutuser_view(self):
        response = self.client.post('/users/logout/')

        self.assertEquals(response.status_code, 302)


    def test_moncompte_view(self):
        response = self.client.get(self.moncompte_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/moncompte.html')


    def test_myproducts_view(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(self.myproducts_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/myproducts.html')

    def test_myproducts_delete_view(self):
        # self.client.login(username='testuser', password='secret')
        # response = self.client.get(self.myproducts_delete_url)

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'users/myproducts.html')

        # Utiliser un mock ??
        pass