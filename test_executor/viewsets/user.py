# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from test_executor.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
