from django.test import TestCase

class SignupTest(TestCase):

    def test_use_signup_template(self):
        """ Testing if """
        response = self.client.get('/users/signup/')
        print(response)
        self.assertTemplateUsed(response, 'users/signup.html')

class LoginTest(TestCase):

    def test_use_signup_template(self):
        """ Testing if """
        response = self.client.get('/users/signup/')
        print(response)
        self.assertTemplateUsed(response, 'users/signup.html')

class LogoutTest(TestCase):

    def test_use_signup_template(self):
        """ Testing if """
        response = self.client.get('/users/signup/')
        print(response)
        self.assertTemplateUsed(response, 'users/signup.html')