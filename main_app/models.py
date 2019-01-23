from django.db import models
from django.contrib.auth.models import User

from unidecode import unidecode
from django.template import defaultfilters

from sorl.thumbnail import ImageField
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(editable=False, null=False)
    color = ColorField(default="#ffffff")

    class Meta:
        verbose_name = 'Категори'
        verbose_name_plural = 'Категори'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(editable=False, null=False)
    parent = models.ForeignKey(Category, null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Дэд категори'
        verbose_name_plural = 'Дэд категори'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(unidecode(self.name))
        super(SubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=120, verbose_name='Гарчиг')
    price = models.IntegerField(verbose_name='Үнэ')
    special = models.BooleanField(verbose_name='Онцгой бүтээгдэхүүн', default=False)
    thumbnail = ImageField(upload_to='thumbnails/', verbose_name='Зураг')
    category = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name='products',
                                 verbose_name='Категори')

    class Meta:
        verbose_name = 'Бүтээгдэхүүн'
        verbose_name_plural = 'Бүтээгдэхүүнүүд'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products_images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Бүтээгдэхүүний зураг'
        verbose_name_plural = 'Бүтээгдэхүүний зураг'

    def __str__(self):
        return self.image.name


class Slide(models.Model):
    image = models.ImageField(upload_to='slides/')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайд'

    def __str__(self):
        return self.image.name
