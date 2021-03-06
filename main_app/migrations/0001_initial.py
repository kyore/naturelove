# Generated by Django 2.1.5 on 2019-01-26 13:04

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(editable=False)),
                ('color', colorfield.fields.ColorField(default='#ffffff', max_length=18)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Категори',
                'verbose_name_plural': 'Категори',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Гарчиг')),
                ('price', models.IntegerField(verbose_name='Үнэ')),
                ('special', models.BooleanField(default=False, verbose_name='Онцгой бүтээгдэхүүн')),
                ('thumbnail', sorl.thumbnail.fields.ImageField(upload_to='thumbnails/', verbose_name='Зураг')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүн',
                'verbose_name_plural': 'Бүтээгдэхүүнүүд',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main_app.Product')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүний зураг',
                'verbose_name_plural': 'Бүтээгдэхүүний зураг',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slides/')),
                ('maromere', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайд',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main_app.Category')),
            ],
            options={
                'verbose_name': 'Дэд категори',
                'verbose_name_plural': 'Дэд категори',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='main_app.SubCategory', verbose_name='Категори'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
