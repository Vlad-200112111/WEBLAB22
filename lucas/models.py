from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.name}'


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
    captions = models.CharField(max_length=500, default="")


class Cart(models.Model):
    product = models.ForeignKey(Product, related_name='carts', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.product.name}'


class Status(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, verbose_name='Имя')
    lname = models.CharField(max_length=200, verbose_name='Фамилия')
    mail = models.CharField(max_length=200, verbose_name='Почта')
    date_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    address = models.CharField(max_length=200, null=True, verbose_name='Адрес')
    zip = models.CharField(max_length=200, null=True, verbose_name='Почтовый индекс')
    comment = models.CharField(max_length=400, null=True, verbose_name='Комментарий')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, verbose_name='Статус')
    total_sum = models.DecimalField(null=True, max_digits=20, decimal_places=2, verbose_name='Итоговая сумма')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'{self.date_create} - {self.status}'


class OrderDetail(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='ИД заказа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    count = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Элемент деталей заказа'
        verbose_name_plural = 'Детали заказов'

    def __str__(self):
        return f'{self.product.name} - {self.product.price}р'
