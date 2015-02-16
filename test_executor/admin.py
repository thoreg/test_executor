# -*- coding: utf-8 -*-
from django.contrib import admin

from test_executor.models import Run


class RunAdmin(admin.ModelAdmin):
    list_display = ('id', 'requester', 'status', 'start_time', 'end_time', 'environment_id')

admin.site.register(Run, RunAdmin)
