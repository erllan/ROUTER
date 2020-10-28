from django.db import models


class Category(models.Model):
    category = models.CharField(verbose_name='катигория', max_length=255)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(verbose_name='Названия', max_length=255)
    description = models.TextField(verbose_name='Описания', )
    photo = models.ImageField(verbose_name='Главное фото', upload_to='album/')
    category = models.ManyToManyField(Category, verbose_name='катигория')

    def __str__(self):
        return self.name


class Album(models.Model):
    name = 'album'
    photo = models.ImageField(verbose_name='фото', upload_to='album/')
    to_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
