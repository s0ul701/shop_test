from django.contrib.auth.models import User
from rest_framework import mixins, throttling, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.permissions import AccountOwnerPermission
from apps.users.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AccountOwnerPermission,)


class TokenThrottle(throttling.AnonRateThrottle):
    """Token throttling class"""
    scope = 'token'


class ProtectedTokenObtainPairView(TokenObtainPairView):
    """Protecting get token method from bruteforce attacks"""
    throttle_classes = (TokenThrottle,)
