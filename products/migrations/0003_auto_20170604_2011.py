# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
