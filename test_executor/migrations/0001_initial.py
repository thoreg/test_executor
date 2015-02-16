# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import test_executor.models
import django_enumfield.db.fields
import django_enumfield.enum
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('status', django_enumfield.db.fields.EnumField(choices=[(0, django_enumfield.enum.Value('PASS', 0, 'PASS', test_executor.models.Status)), (1, django_enumfield.enum.Value('FAIL', 1, 'FAIL', test_executor.models.Status)), (2, django_enumfield.enum.Value('RUNNING', 2, 'RUNNING', test_executor.models.Status))], enum=test_executor.models.Status, default=2)),
                ('environment_id', models.PositiveSmallIntegerField()),
                ('output', models.TextField(blank=True, null=True)),
                ('requester', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file_name', models.CharField(max_length=2048)),
                ('run', models.ForeignKey(to='test_executor.Run')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
