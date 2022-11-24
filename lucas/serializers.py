from rest_framework import serializers

from .models import Product, Cart, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['__all__']


class ProductsSerializer(serializers.ModelSerializer):
    # carts

    class Meta:
        model = Product
        fields = ['id', 'path_img', 'name', 'price', 'old_price']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'product', 'profile']

