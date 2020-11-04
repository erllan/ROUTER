# Generated by Django 3.0.2 on 2020-10-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_router', '0006_auto_20201030_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=14, verbose_name='Телефон')),
                ('Email', models.EmailField(max_length=255, verbose_name='Почта')),
                ('delivery_city', models.CharField(max_length=255, verbose_name='Город доставки')),
                ('Comment', models.CharField(max_length=255, verbose_name='Комментарий к заказу')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')),
                ('order', models.ManyToManyField(to='shop_router.Product')),
            ],
        ),
    ]