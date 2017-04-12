# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-12 13:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bets', '0003_auto_20170407_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bets_bet_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bet',
            name='result',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bet',
            name='result_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bets_bet_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
