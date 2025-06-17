import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from products.models import Product  # model nomi sizda boshqacha bo‘lishi mumkin

@pytest.mark.django_db
class TestProductAPI:
    def setup_method(self):
        self.client = APIClient()

    def test_list_products(self):
        url = reverse('product-list')  # URL name sizda boshqacha bo‘lishi mumkin
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            "name": "Test Product",
            "price": 99.99,
            "description": "A test product"
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == 201
        assert response.data["name"] == "Test Product"

    def test_get_single_product(self):
        product = Product.objects.create(name="Single", price=10.0)
        url = reverse('product-detail', args=[product.id])
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data["name"] == "Single"

    def test_update_product(self):
        product = Product.objects.create(name="Old", price=5.0)
        url = reverse('product-detail', args=[product.id])
        data = {"name": "Updated", "price": 7.0}
        response = self.client.put(url, data, format='json')
        assert response.status_code == 200
        assert response.data["name"] == "Updated"

    def test_delete_product(self):
        product = Product.objects.create(name="DeleteMe", price=12.0)
        url = reverse('product-detail', args=[product.id])
        response = self.client.delete(url)
        assert response.status_code == 204