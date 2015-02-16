# -*- coding: utf-8 -*-

from rest_framework import serializers

from test_executor.models import Run


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('id', 'requester', 'start_time', 'end_time', 'status', 'environment_id')
