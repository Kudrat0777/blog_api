from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('apps.api.urls', namespace='api')),
    path('api/v1/', include('rest_framework.urls')),
]


urlpatterns += [
    path('admin/', admin.site.urls),
]
