# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField()),
                ('level_type', models.SmallIntegerField()),
                ('resolution_type', models.SmallIntegerField()),
                ('number', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('created_at', models.BigIntegerField()),
                ('updated_at', models.BigIntegerField()),
            ],
        ),
    ]
