# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-04 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]