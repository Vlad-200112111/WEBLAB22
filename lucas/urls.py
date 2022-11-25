from django.urls import path

from lucas.views import CartAPIView, CartListAPIView, ProductCreateAPIView, CartCreateAPIView, \
    ProductListAPIView, ProductAPIView, ProductListByCatAPIView, CheckoutCreateAPIView

app_name = 'lucas'

urlpatterns = [
    path('cart/<int:pk>', CartAPIView.as_view()),
    path('product/<int:pk>', ProductAPIView.as_view()),
    path('cart/', CartListAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/categories', ProductListByCatAPIView.as_view()),
    path('product/create/', ProductCreateAPIView.as_view()),
    path('cart/create/', CartCreateAPIView.as_view()),
    path('checkout/create/', CheckoutCreateAPIView.as_view()),
]
