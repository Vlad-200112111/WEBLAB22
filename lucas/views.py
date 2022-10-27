from django.views.generic import TemplateView
from rest_framework import generics

from lucas.models import Product, Cart
from lucas.serializers import ProductsSerializer, CartSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

class CartAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductsSerializer

class CartCreateAPIView(generics.CreateAPIView):
    serializer_class = CartSerializer
