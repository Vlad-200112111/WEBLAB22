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
