from django.urls import path
from apps.api import views

app_name = 'api'

urlpatterns = [
    path('users/', views.UserListApiView.as_view()),
    path('users/<int:pk>/', views.UserDetailApiView.as_view())
]
