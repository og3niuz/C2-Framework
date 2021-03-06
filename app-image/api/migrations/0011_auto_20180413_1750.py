# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-13 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180403_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_string', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='module',
            name='id',
        ),
        migrations.AddField(
            model_name='module',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
