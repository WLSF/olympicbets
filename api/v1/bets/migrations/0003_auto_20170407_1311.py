# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-07 13:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_auto_20170407_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bet',
            old_name='bettype',
            new_name='bet_type',
        ),
    ]
