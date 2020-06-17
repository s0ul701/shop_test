from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from apps.invoices.models import Invoice
from apps.invoices.permissions import InvoiceOwnPermission
from apps.invoices.serializers import InvoiceSerializer


class InvoiceViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    permission_classes = (IsAdminUser | InvoiceOwnPermission,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()

        return Invoice.objects.filter(
            customer=self.request.user
        ).prefetch_related('positions')
