from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import generics
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


@method_decorator(swagger_auto_schema(request_body=ProductSerializer), name='post')
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@method_decorator(swagger_auto_schema(request_body=ProductSerializer), name='put')
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'code'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
