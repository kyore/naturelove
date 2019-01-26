from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', null=True, on_delete=models.SET_NULL, verbose_name='Үүсгэгч')
    title = models.CharField(max_length=120, verbose_name='Гарчиг')
    content = RichTextUploadingField(verbose_name='Контент')
    thumbnail = ImageField(verbose_name='Зураг')
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self): return self.title
