# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 12:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0010_auto_20170615_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='triggered_at_time',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
