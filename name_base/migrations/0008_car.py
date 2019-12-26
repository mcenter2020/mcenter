# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('name_base', '0007_name_list_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name_base.Name_list', verbose_name='Список')),
            ],
        ),
    ]
