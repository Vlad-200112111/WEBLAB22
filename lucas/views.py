from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Product, Cart
from .serializers import ProductsSerializer, CartSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
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


class CartListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = Cart.objects.all()
        queryset = queryset.filter(profile_id=self.request.user.id)
        return queryset


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductsSerializer


class CartCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        request.data['profile'] = request.user.id
        return super().create(request, *args, **kwargs)
