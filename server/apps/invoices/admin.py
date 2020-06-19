from django.contrib import admin

from apps.invoices.models import Invoice, InvoicePosition


class InvoicePositionInline(admin.TabularInline):
    model = InvoicePosition


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoicePositionInline,)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
