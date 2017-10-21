# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('notes', models.CharField(max_length=250)),
                ('supplier', models.CharField(max_length=250)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('currency', models.CharField(max_length=250)),
            ],
        ),
    ]
