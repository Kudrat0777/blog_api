from django.urls import path
from apps.api import views

app_name = 'api'

urlpatterns = [
    path('users/', views.UserListApiView.as_view()),
    path('users/<int:pk>/', views.UserDetailApiView.as_view()),

    path('posts/', views.PostListApiView.as_view()),
    path('posts/<int:pk>/', views.PostDetailApiView.as_view()),

    path('comments/', views.CommentListApiView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailApiView.as_view()),
]
