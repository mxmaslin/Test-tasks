# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_tag', '0002_auto_20171126_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]