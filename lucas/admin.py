from django.contrib import admin

from .models import Profile, Product, Cart, Category, Checkout, BillingAddressCheckout, BillingAddress

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Checkout)
admin.site.register(BillingAddress)
admin.site.register(BillingAddressCheckout)
