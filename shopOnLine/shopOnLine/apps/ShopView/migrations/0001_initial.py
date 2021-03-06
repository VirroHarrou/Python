# Generated by Django 3.2.9 on 2021-12-05 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=255, verbose_name='наименование товара')),
                ('product_description', models.TextField(verbose_name='описание товара')),
                ('product_picture', models.ImageField(upload_to='', verbose_name='картинка товара')),
                ('pub_date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='product_features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Avtor_name', models.CharField(max_length=70, verbose_name='имя автора')),
                ('comment_text', models.CharField(max_length=500, verbose_name='текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopView.product')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avtor_name', models.CharField(max_length=70, verbose_name='имя автора')),
                ('comment_text_positive', models.CharField(max_length=500, verbose_name='положительные стороны')),
                ('comment_text_negative', models.CharField(max_length=500, verbose_name='недостатки')),
                ('comment_text', models.CharField(max_length=500, verbose_name='текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopView.product')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
