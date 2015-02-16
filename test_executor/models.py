# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django_enumfield import enum


class Status(enum.Enum):
    PASS = 0
    FAIL = 1
    RUNNING = 2


class Run(models.Model):
    requester = models.ForeignKey(User)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = enum.EnumField(Status, default=Status.RUNNING)
    environment_id = models.PositiveSmallIntegerField()
    output = models.TextField(blank=True, null=True)


class Test(models.Model):
    run = models.ForeignKey(Run)
    file_name = models.CharField(max_length=2048)
