# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0007_museo_id_externo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='id_externo',
            field=models.CharField(default='no-id', max_length=150),
            preserve_default=False,
        ),
    ]
