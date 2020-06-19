from django.http.response import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (decorators, filters, mixins, response, status,
                            viewsets)
from rest_framework.permissions import IsAdminUser

from apps.invoices.models import Invoice
from apps.invoices.permissions import InvoiceOwnPermission
from apps.invoices.serializers import InvoiceSerializer

from .utils import get_invoice_pdf_str


class InvoiceViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    permission_classes = (IsAdminUser | InvoiceOwnPermission,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('customer',)
    ordering_fields = ('deal_date',)

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()

        return Invoice.objects.filter(
            customer=self.request.user
        ).prefetch_related('positions')

    @decorators.action(detail=True, methods=('GET',))
    def get_pdf_report(self, request, pk=None):
        invoice = self.get_object()
        if not invoice:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        pdf_str = get_invoice_pdf_str(invoice)
        response_ = HttpResponse(content=pdf_str, content_type='application/pdf')
        response_['Content-Disposition'] = 'attachment;filename=some_file.pdf'
        return response_
