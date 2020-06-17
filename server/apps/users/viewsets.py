from django.contrib.auth.models import User
from rest_framework import mixins, viewsets

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
