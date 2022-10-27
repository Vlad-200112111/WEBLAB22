from rest_framework import serializers

from lucas.models import Product, Cart


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'path_img', 'name', 'price', 'old_price']


class CartSerializer(serializers.ModelSerializer):
    # product = ProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'path_img', 'name', 'price', 'old_price']

