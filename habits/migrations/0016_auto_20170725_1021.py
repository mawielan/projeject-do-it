# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0015_auto_20170725_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='comments',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='related_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.Habit'),
        ),
    ]
