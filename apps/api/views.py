from itertools import permutations
from rest_framework import generics, permissions
from apps.api import serializers
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from .models import Post, Comment, Category, Service, Portfolio


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
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ServiceListApiView(generics.ListCreateAPIView):
    """Service List"""
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ServiceDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """Service Detail"""
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PortfolioListApiView(generics.ListCreateAPIView):
    """Portfolio"""
    queryset = Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PortfolioDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """Portfolio"""
    queryset = Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]