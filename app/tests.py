from django.urls import reverse, resolve
from django.test import TestCase
from .views import *

class Test(TestCase):
    def test_api_over_view(self):
        url = reverse('api_over_view')
        self.assertEqual(resolve(url).func, api_over_view)

    def test_register(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
    
    def test_product_list(self):
        url = reverse('product_list')
        self.assertEqual(resolve(url).func, product_list)
    
    def test_order(self):
        url = reverse('order')
        self.assertEqual(resolve(url).func, order)
    
    def test_payment_transaction(self):
        url = reverse('payment_transaction')
        self.assertEqual(resolve(url).func, payment_transaction)

