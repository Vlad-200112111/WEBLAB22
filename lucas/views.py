from django.db.models import Sum
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Product, Cart, Category, Checkout, BillingAddress, BillingAddressCheckout
from .serializers import ProductsSerializer, CartSerializer, CheckoutSerializer, BillingAddressSerializer, \
    BillingAddressCheckoutSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['category'] = Category.objects.all()
        return context


class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carts'] = Cart.objects.all().filter(profile_id=self.request.user.id)
        print("sssssssssssssss", Cart.objects.all().filter(profile_id=self.request.user.id))
        context['price'] = Cart.objects.all().filter(profile_id=self.request.user.id).aggregate(Sum('product__price'))
        return context


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


class CartAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class ProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductListByCatAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.all()
        queryset = queryset.filter(category_id=self.kwargs['pk'], news=True)
        return queryset


class CartListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = Cart.objects.all()
        queryset = queryset.filter(profile_id=self.request.user.id)
        return queryset


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductsSerializer


class CheckoutCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CheckoutSerializer


class CheckoutListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CheckoutSerializer

    # def get_queryset(self):
    #     queryset = Checkout.objects.all()
    #     queryset = queryset.filter(profile_id=self.request.user.id)
    #     return queryset


class BillingAddressCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BillingAddressSerializer
    queryset = BillingAddress.objects.all()


class BillingAddressCheckoutCreateApiView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BillingAddressCheckoutSerializer
    queryset = BillingAddressCheckout.objects.all()


class CartCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        request.data['profile'] = request.user.id
        return super().create(request, *args, **kwargs)
