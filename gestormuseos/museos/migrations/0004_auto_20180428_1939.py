# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0003_auto_20180428_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='favoritos',
            field=models.ManyToManyField(related_name='configuraciones', to='museos.Museo'),
        ),
    ]
