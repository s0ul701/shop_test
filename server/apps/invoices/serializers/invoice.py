from django.contrib.auth.models import User
from rest_framework import serializers

from .invoice_position import InvoicePositionSerializer
from apps.invoices.models import Invoice, InvoicePosition
from apps.users.serializers import UserSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    """Serializer for create/retrieve/list Invoice"""
    positions = InvoicePositionSerializer(many=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Invoice
        fields = ('customer', 'positions', 'deal_date',)

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        invoice = Invoice.objects.create(**validated_data)
        for position in positions:
            InvoicePosition.objects.create(**position, invoice=invoice)
        return invoice

    def to_representation(self, instance):
        """Transform Customer ID to full Customer object for representation"""
        dict_ = super().to_representation(instance)
        dict_.update({
            'customer': UserSerializer(
                User.objects.get(id=dict_['customer'])
            ).data
        })
        return dict_
