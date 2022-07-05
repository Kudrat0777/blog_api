from rest_framework import generics
from apps.api import serializers
from django.contrib.auth.models import User
from .models import Post


class UserListApiView(generics.ListAPIView):
    """User List"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailApiView(generics.RetrieveAPIView):
    """User Detail"""
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostListApiView(generics.ListCreateAPIView):
    """Post List"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """Post Detail"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer