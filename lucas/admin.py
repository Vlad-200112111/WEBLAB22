from django.contrib import admin

from .models import *

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Status)

