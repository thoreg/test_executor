# -*- coding: utf-8 -*-
import logging
import os
import subprocess
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User

from test_executor.models import Run, Status, Test

log = logging.getLogger(__name__)


def collect_test_files():
    log.debug("TEST_DIR: {}".format(settings.TEST_DIR))
    test_files = []
    for dirpath, subdirs, files in os.walk(settings.TEST_DIR):
        for x in files:
            if x.endswith(".py") and x.startswith('test_'):
                test_files.append(os.path.join(dirpath, x))

    return sorted(test_files)


def create_run(requester_id, environment_id):

    requester = User.objects.get(id=requester_id)
    run = Run(requester=requester, status=Status.RUNNING, environment_id=environment_id)
    run.save()

    test_file_names = collect_test_files()
    test_objects = []
    for file_name in test_file_names:
        test_objects.append(Test(run=run, file_name=file_name))

    Test.objects.bulk_create(test_objects)

    try:
        output = subprocess.check_output("py.test -s -vv %s" % ' '.join(test_file_names),
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        run.status = Status.PASS
    except subprocess.CalledProcessError as e:
        output = e.output
        run.status = Status.FAIL

    run.output = output.decode('utf-8')
    run.end_time = datetime.now()
    run.save()
