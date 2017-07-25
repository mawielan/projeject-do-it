# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 12:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Existingroutine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('trigger', models.CharField(choices=[('After I', 'After I'), ('When I', 'When I'), ('Whenever I', 'Whenever I'), ('Before I', 'Before I'), ('Meanwhile I', 'Meanwhile I')], default='After I', max_length=15)),
                ('image', models.ImageField(blank=True, upload_to='habit_image')),
                ('status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=3)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.UserProfile')),
                ('existingroutine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.Existingroutine')),
            ],
        ),
        migrations.CreateModel(
            name='Targetbehavior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='habit',
            name='targetbehavior',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.Targetbehavior'),
        ),
    ]