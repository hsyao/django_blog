# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20170625_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default.png', upload_to='avatar'),
        ),
    ]
