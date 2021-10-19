from django.urls import reverse, resolve
from django.test import TestCase
from .views import *

class Test(TestCase):
    def test_analytics(self):
        url = reverse('analytics')
        self.assertEqual(resolve(url).func, analytics)
    
    def test_ledger(self):
        url = reverse('ledger')
        self.assertEqual(resolve(url).func, ledger)
