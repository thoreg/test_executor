# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns
from rest_framework import routers

from test_executor.viewsets import RunViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'runs', RunViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('', (r'^', include(router.urls)))
