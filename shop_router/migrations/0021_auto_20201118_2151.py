# Generated by Django 3.0.2 on 2020-11-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_router', '0020_auto_20201118_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='shop_router.Category', verbose_name='катигория'),
        ),
    ]
