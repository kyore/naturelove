# Generated by Django 2.1.5 on 2019-01-22 12:34

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190122_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=colorfield.fields.ColorField(default='#ffffff', max_length=18),
        ),
    ]
