# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task

from test_executor.services import create_run


@shared_task
def create_test_execution(requester_id, environment_id):
    return create_run(requester_id, environment_id)
