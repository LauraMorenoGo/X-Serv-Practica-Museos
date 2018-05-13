# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0006_auto_20180428_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='museo',
            name='id_externo',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
