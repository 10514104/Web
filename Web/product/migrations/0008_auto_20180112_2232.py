# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-12 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20180112_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productimg',
            field=models.ImageField(height_field=500, upload_to='', width_field=500),
        ),
    ]
