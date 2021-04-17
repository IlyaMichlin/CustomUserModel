from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


# Create your tests here.
class HomePageTest(SimpleTestCase):
    def test_home_page_status_code(self):
        resource = self.client.get('/')
        self.assertEqual(resource.status_code, 200)

    def test_view_url_by_name(self):
        resource = self.client.get(reverse('home'))
        self.assertEqual(resource.status_code, 200)

    def test_view_uses_correct_template(self):
        resource = self.client.get(reverse('home'))
        self.assertEqual(resource.status_code, 200)
        self.assertTemplateUsed(resource, 'home.html')


class SignUpPageTest(TestCase):
    username = 'new_user'
    email = 'new_user@mail.com'

    def test_sign_up_page_status_code(self):
        resource = self.client.get('/accounts/signup/')
        self.assertEqual(resource.status_code, 200)

    def test_view_url_by_name(self):
        resource = self.client.get(reverse('signup'))
        self.assertEqual(resource.status_code, 200)

    def test_view_uses_correct_template(self):
        resource = self.client.get(reverse('signup'))
        self.assertEqual(resource.status_code, 200)
        self.assertTemplateUsed(resource, 'registration/signup.html')

    def test_sign_up_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
