from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Profile(AbstractUser):
    patronymic = models.CharField(max_length=150, )
    pass


class Product(models.Model):
    path_img = models.ImageField(upload_to='static/img/')
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    old_price = models.IntegerField()
    news = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Cart(models.Model):
    product = models.ForeignKey(Product, related_name='carts', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Checkout(models.Model):
    carts = models.ForeignKey(Cart, on_delete=models.CASCADE)


class BillingAddress(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_create_account = models.BooleanField(default=False)
    order_notes = models.CharField(max_length=50)

    def __str__(self):
        return self.address


class BillingAddressCheckout(models.Model):
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)



