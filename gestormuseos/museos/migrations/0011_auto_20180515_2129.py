# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0010_auto_20180515_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='favoritos',
        ),
        migrations.AddField(
            model_name='favorito',
            name='configuracion',
            field=models.ForeignKey(related_name='favoritos', to='museos.Configuracion'),
        ),
        migrations.AddField(
            model_name='favorito',
            name='museo',
            field=models.ForeignKey(related_name='favoritos', to='museos.Museo'),
        ),
    ]
