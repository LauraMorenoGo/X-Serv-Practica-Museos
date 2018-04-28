# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='favoritos',
            field=models.ManyToManyField(related_name='configuraciones', to='museos.Museo', null=True),
        ),
    ]
