# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-05 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0005_auto_20181104_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inst',
            name='id',
        ),
        migrations.AlterField(
            model_name='inst',
            name='id_inst',
            field=models.TextField(primary_key=True, serialize=False, unique=True),
        ),
    ]
