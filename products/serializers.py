from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'code',
            'barcode',
            'product_name',
            'url',
            'quantity',
            'categories',
            'packaging',
            'brands',
            'image_url',
            'imported_t',
            'status',

        ]
