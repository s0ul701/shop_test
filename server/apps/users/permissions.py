from rest_framework.permissions import SAFE_METHODS, BasePermission


class AccountOwnerPermission(BasePermission):
    """Allow list/retreive for all and update for owner"""
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user
