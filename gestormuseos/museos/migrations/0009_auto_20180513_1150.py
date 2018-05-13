# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0008_auto_20180513_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='fondo',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='letra',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='nombre_pag',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
