from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.viewsets import UserViewSet

app_name = 'api_v1'

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
