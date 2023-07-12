from rest_framework import status
import json
from django.test import TestCase, Client
from django.urls import reverse


client = Client()


class ProductTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            "code": 3661112502850,
            "barcode": "3661112502850(EAN / EAN-13)",
            "url": "https://world.openfoodfacts.org/product/3661112502850",
            "product_name": "Jambon de Paris cuit à l'étouffée",
            "quantity": "240 g",
            "categories": "Meats, Prepared meats, Hams, White hams",
            "packaging": "Film en plastique, Film en plastique",
            "brands": "Tradilège, Marque Repère",
            "image_url": "https://static.openfoodfacts.org/images/products/366/111/250/2850/front_fr.3.400.jpg"
        }

        self.invalid_payload = {
            "code": "",
            "barcode": "3661112502850(EAN / EAN-13)",
            "url": "https://world.openfoodfacts.org/product/3661112502850",
            "product_name": "",
            "quantity": "240 g",
            "categories": "Meats, Prepared meats, Hams, White hams",
            "packaging": "Film en plastique, Film en plastique",
            "brands": "Tradilège, Marque Repère",
            "image_url": "https://static.openfoodfacts.org/images/products/366/111/250/2850/front_fr.3.400.jpg"
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('products:list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('products:list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_products(self):
        response = client.get(
            reverse('products:list'),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
