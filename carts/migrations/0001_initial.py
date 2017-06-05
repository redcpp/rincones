# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20170604_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(blank=True, null=True, to='products.Product')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
    ]
