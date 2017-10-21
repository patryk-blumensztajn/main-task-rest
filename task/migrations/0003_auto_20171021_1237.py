# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='price',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
