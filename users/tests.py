from django.test import TestCase

class SignupTest(TestCase):

    def test_use_signup_template(self):
        response = self.client.get('/users/signup/')
        print(response)
        self.assertTemplateUsed(response, 'users/signup.html')
