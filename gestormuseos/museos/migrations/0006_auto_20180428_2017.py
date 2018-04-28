# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0005_auto_20180428_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='equipamiento',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='horario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
