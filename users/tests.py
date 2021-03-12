from django.test import TestCase

class SignupTest(TestCase):

    def test_use_signup_template(self):
        response = self.client.get('/users/signup/')
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_is_it_a_POST_method(self):
        pass

    def test_if_passwords_didnt_match(self):
        pass

    def test_if_user_already_exist_in_db(self):
        pass

    def test_a_loguser_cant_see_page(self):
        pass

class LoginTest(TestCase):

    def test_use_login_template(self):
        response = self.client.get('/users/login/')
        self.assertTemplateUsed(response, 'users/login.html')

class LogoutTest(TestCase):

    def test_use_logout_template(self):
        pass