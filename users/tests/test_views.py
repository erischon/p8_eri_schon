from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User, AnonymousUser

from database.models import Product, Nutriscore
from users.views import signupuser, myproducts_delete

class UsersTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.user = User.objects.get(username='testuser')

        nutriscore = Nutriscore.objects.create(nut_id=1, nut_type="C")
        self.product = Product.objects.create(
            prod_id = 3017620422003,
            prod_name = "test product",
            nut_id = nutriscore,
        )
        self.product.myproduct.add(self.user)

        self.signupuser_url = reverse('signupuser')
        self.moncompte_url = reverse('moncompte')
        self.myproducts_url = reverse('myproducts')


    ### Method signupuser ###
    def test_signupuser_view(self):
        response = self.client.get(self.signupuser_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signupuser_view_post_method_no_same_kw(self):
        response = self.client.post('/users/signup/', {'password1': 'pass1', 'password2': 'pass2'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signupuser_view_post_method_except(self):
        response = self.client.post('/users/signup/', {'password1': 'pass1', 'password2': 'pass1', 'username': 'testuser'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signupuser_view_post_method_with_connect(self):
        response = self.client.post('/users/signup/', {'password1': 'pass1', 'password2': 'pass1', 'username': 'testuser2'})

        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response, 'users/signup.html')

        # request = self.factory.post('/users/signup/', {'password1': 'pass1', 'password2': 'pass1', 'username': 'testuser2'})

        # response = signupuser(request)

        # self.assertEquals(response.status_code, 200)


    ### Method loginuser ###
    def test_loginuser_view(self):
        response = self.client.post('/users/login/', self.credentials, follow= True)

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
        self.client.login(**self.credentials)
        response = self.client.get(self.myproducts_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/myproducts.html')

    def test_myproducts_delete_view(self):
        self.client.login(**self.credentials)
        request = self.factory.get('/search/result/')

        response = myproducts_delete(request, self.product.prod_id)

        self.assertEquals(response.status_code, 302)
