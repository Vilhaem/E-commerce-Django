from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        user_class = get_user_model()
        user = user_class.objects.create_superuser("test_user","testmail@test.com","Aa135792468")
        client = Client()
        client.login(username=user.username, password=user.password)
        Product.objects.create(
            user=user,
            name="test_product",
            handle="test-product",
            )
        self.product = Product.objects.get(name="test_product")


    def test_product_property(self):
        """Products have the correct name and shit"""
        self.assertEqual(self.product.user.username, 'test_user')
        self.assertEqual(self.product.name, 'test_product')
        self.assertEqual(self.product.handle, 'test-product')
    def test_product_update(self):
        og_time = self.product.timestamp
        