from rest_framework import serializers

from .models import Product, Cart, Profile, Checkout, BillingAddress, BillingAddressCheckout


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['__all__']


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id', 'carts']


class ProductsSerializer(serializers.ModelSerializer):
    # carts

    class Meta:
        model = Product
        fields = ['id', 'path_img', 'name', 'price', 'old_price']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'product', 'profile']


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = '__all__'

class BillingAddressCheckoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingAddressCheckout
        fields = '__all__'
