from django.contrib import admin
from django.urls import path, include

from lucas.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('lucas.urls')),
    path('', IndexView.as_view(), name='index'),
]
