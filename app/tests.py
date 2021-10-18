from django.test import TestCase
from .views import register
from django.urls import reverse, resolve
def add_two_numbers(a, b):
    return a + b


class TestExample(TestCase):

    def test_add_two_numbers(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    # def test_register(self):
    #     self.assertIn('posts')
