from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class InvoiceOwnPermission(IsAuthenticated):
    """Allow list/retreive only own invoice for customer"""
    def has_object_permission(self, request, view, obj):
        if obj.customer == request.user and request.method in SAFE_METHODS:
            return True
        return obj == request.user
