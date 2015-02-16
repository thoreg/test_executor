# -*- coding: utf-8 -*-
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from test_executor.models import Run, Status
from test_executor.serializers import RunSerializer
from test_executor.tasks import create_test_execution


class RunViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    model = Run
    queryset = Run.objects.all().order_by('-start_time')
    serializer_class = RunSerializer

    def create(self, request):
        requester_id = request.POST.get('requester_id', None)
        environment_id = request.POST.get('environment_id', None)

        if not requester_id:
            return Response({'message': 'Requester ID invalid'},
                            status=status.HTTP_411_LENGTH_REQUIRED)

        if not environment_id:
            return Response({'message': 'Environment ID invalid'},
                            status=status.HTTP_411_LENGTH_REQUIRED)

        if Run.objects.filter(environment_id=environment_id, status=Status.RUNNING).exists():
            message = 'There is already a test execution running for this environment.'
            return Response({'message': message}, status=status.HTTP_409_CONFLICT)

        create_test_execution.delay(requester_id, environment_id)

        return Response({'message': 'Test execution successful'}, status=status.HTTP_200_OK)
