# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0009_auto_20180513_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museo',
            name='accesibilidad',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='barrio',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='clase_via',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='content_url',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='coordenada_x',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='coordenada_y',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='distrito',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='latitud',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='localidad',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='longitud',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='nombre_via',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='provincia',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='tipo',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
