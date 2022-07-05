from rest_framework import generics, permissions
from apps.api import serializers
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from .models import Post, Comment, Category


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """Post Detail"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentListApiView(generics.ListCreateAPIView):
    """Comment List"""
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """Comment Detail"""
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CategoryListApiView(generics.ListCreateAPIView):
    """Category List"""
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """Category Deatail"""
    queryset = Category.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
