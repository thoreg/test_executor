# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('test_executor.views',
                       url(r'^/runs/(?P<run_id>.+)/$', 'detail', name="test_execution_detail"),
                       url(r'^/runs/$', 'overview', name="test_execution_overview"),)
