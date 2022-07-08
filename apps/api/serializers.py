from rest_framework import serializers
from django.contrib.auth.models import User

from apps.api.models import Category, Post, Comment, Service


class UserSerializer(serializers.ModelSerializer):
    """Users"""
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'categories']


class PostSerializer(serializers.ModelSerializer):
    """Posts"""
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'image',
        'owner', 'comments', 'categories']


class CommentSerializer(serializers.ModelSerializer):
    """Comments"""

    class Meta:
        model = Comment
        fields = ['id', 'body', 'post']


class CategorySerializer(serializers.ModelSerializer):
    """Categoryes"""
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'posts']


class ServiceSerializer(serializers.ModelSerializer):
    """Services"""
    class Meta:
        model = Service
        fields = ['id', 'title', 'body']

