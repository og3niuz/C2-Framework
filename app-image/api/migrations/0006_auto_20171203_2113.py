# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171203_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_Command_History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=True)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agent')),
            ],
        ),
        migrations.AlterField(
            model_name='command',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Group'),
        ),
        migrations.AddField(
            model_name='agent_command_history',
            name='command_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Command'),
        ),
    ]
