# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0012_auto_20170615_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
