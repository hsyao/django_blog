# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20170625_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', upload_to='avatar', verbose_name='头像'),
        ),
    ]
