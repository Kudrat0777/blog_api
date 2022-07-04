from rest_framework import generics
from apps.api import serializers
from django.contrib.auth.models import User


class UserListApiView(generics.ListAPIView):
    """User List"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailApiView(generics.RetrieveAPIView):
    """User Detail"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer