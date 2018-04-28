# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0004_auto_20180428_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='horario',
            field=models.TextField(null=True),
        ),
    ]
