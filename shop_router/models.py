from django.db import models
from datetime import datetime


class Catalog(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    category = models.CharField(verbose_name='катигория', max_length=255)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.category


class Brand(models.Model):
    brand_name = models.CharField(verbose_name='бренд', max_length=255)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name='Названия', max_length=255)
    description = models.TextField(verbose_name='Описания', )
    category = models.ManyToManyField(Category, verbose_name='катигория')
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255, null=True)
    interface = models.CharField(max_length=255, null=True)
    safety = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(verbose_name='Дата', default=datetime.now)
    hit = models.BooleanField(default=False)
    sale = models.IntegerField('Скидка в процентах', blank=True, default=0)

    def get_sale(self):
        proc = int((self.sale * self.price) / 100)
        price = self.price - proc
        return price


def __str__(self):
    return self.title


class Album(models.Model):
    name = 'album'
    photo = models.ImageField(verbose_name='фото', upload_to='album/')
    to_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=14)
    Email = models.EmailField(verbose_name='Почта', max_length=255)
    delivery_city = models.CharField(verbose_name='Город доставки', max_length=255)
    Comment = models.CharField(verbose_name='Комментарий к заказу', max_length=255)
    order_date = models.DateTimeField(verbose_name='Дата и время заказа', default=datetime.now)

    def __str__(self):
        return self.full_name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    from_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_quantities = models.IntegerField()
