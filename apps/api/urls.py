from django.urls import path
from apps.api import views

app_name = 'api'

urlpatterns = [
    # User urls
    path('users/', views.UserListApiView.as_view()),
    path('users/<int:pk>/', views.UserDetailApiView.as_view()),
    # Post urls
    path('posts/', views.PostListApiView.as_view()),
    path('posts/<int:pk>/', views.PostDetailApiView.as_view()),
    # Comments urls
    path('comments/', views.CommentListApiView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailApiView.as_view()),
    # Categories urls
    path('categories/', views.CategoryListApiView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailApiView.as_view()),
    # Services urls
    path('services/', views.ServiceListApiView.as_view()),
    path('services/<int:pk>/', views.ServiceDetailApiView.as_view()),
]
