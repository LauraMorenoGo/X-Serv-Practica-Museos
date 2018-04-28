# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0002_auto_20180428_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museo',
            name='equipamiento2',
        ),
        migrations.AddField(
            model_name='museo',
            name='descripcion_entidad',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='favoritos',
            field=models.ManyToManyField(blank=True, null=True, to='museos.Museo', related_name='configuraciones'),
        ),
        migrations.AlterField(
            model_name='museo',
            name='barrio',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='clase_via',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='codigo_postal',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='content_url',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='distrito',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='email',
            field=models.CharField(blank=True, null=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='equipamiento',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='museo',
            name='horario',
            field=models.CharField(blank=True, null=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='localidad',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='nombre_via',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='numero_via',
            field=models.CharField(blank=True, null=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='provincia',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='telefono',
            field=models.CharField(blank=True, null=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='tipo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='museo',
            name='transporte',
            field=models.CharField(blank=True, null=True, max_length=150),
        ),
    ]
