# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32)),
                ('descripcion', models.TextField(null=True)),
                ('horario', models.CharField(null=True, max_length=32, blank=True)),
                ('equipamiento', models.TextField()),
                ('transporte', models.CharField(null=True, max_length=32, blank=True)),
                ('equipamiento2', models.TextField()),
                ('accesibilidad', models.IntegerField()),
                ('content_url', models.TextField()),
                ('nombre_via', models.CharField(max_length=32)),
                ('clase_via', models.CharField(max_length=32)),
                ('numero_via', models.IntegerField()),
                ('localidad', models.CharField(max_length=32)),
                ('provincia', models.CharField(max_length=32)),
                ('codigo_postal', models.CharField(max_length=32)),
                ('barrio', models.CharField(max_length=32)),
                ('distrito', models.CharField(max_length=32)),
                ('coordenada_x', models.IntegerField()),
                ('coordenada_y', models.IntegerField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('telefono', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('tipo', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='configuracion',
            name='favoritos',
            field=models.ManyToManyField(to='museos.Museo', related_name='configuraciones'),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='usuario',
            field=models.OneToOneField(related_name='config', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='configuracion',
            field=models.ForeignKey(related_name='comentarios', to='museos.Configuracion'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='museo',
            field=models.ForeignKey(related_name='comentarios', to='museos.Museo'),
        ),
    ]
