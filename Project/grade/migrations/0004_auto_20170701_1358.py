# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-01 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0003_auto_20170628_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]