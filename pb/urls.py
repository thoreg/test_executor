# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^accounts/login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout',
                           {'next_page': '/'}),

                       url(r'^api/test_executor/', include('test_executor.urls.api')),
                       url('^test_executor', include('test_executor.urls.ui')),

                       url('^$', 'pb.views.index', name="index"))
