from django.contrib import admin
from django.urls import include, path

from apps import api_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1.urls, namespace='api_v1')),
]
