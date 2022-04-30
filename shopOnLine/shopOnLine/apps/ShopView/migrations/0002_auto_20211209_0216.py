# Generated by Django 3.2.9 on 2021-12-08 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopView', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='product_features',
            options={'verbose_name': 'Описание продукта', 'verbose_name_plural': 'Описание продуктов'},
        ),
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(upload_to='image/%Y-%m-%d/', verbose_name='картинка товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
