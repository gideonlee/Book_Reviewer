# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0002_auto_20160929_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(),
        ),
    ]
