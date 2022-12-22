from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from lucas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('lucas.urls')),
    path('token/', obtain_auth_token),
    path('', IndexView.as_view()),
    path('checkout/', CheckoutView.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
]
