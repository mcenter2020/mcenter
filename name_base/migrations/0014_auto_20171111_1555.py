# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name_base', '0013_auto_20171111_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name_list',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Фотография'),
        ),
    ]
