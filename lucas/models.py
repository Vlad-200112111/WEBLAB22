from django.db import models


class Product(models.Model):
    path_img = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    old_price = models.IntegerField()

class Cart(models.Model):
    path_img = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    old_price = models.IntegerField()




