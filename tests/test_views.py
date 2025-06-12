# test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

class SimpleViewTest(TestCase):
    def test_product_list_view(self):
        Product.objects.create(name="Telefon", price=1000, stock=5)
        client = Client()
        response = client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")