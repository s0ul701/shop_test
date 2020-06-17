from rest_framework import serializers

from apps.invoices.models import InvoicePosition
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class InvoicePositionSerializer(serializers.ModelSerializer):
    """Serializer for retrieve/list InvoicePosition"""
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = InvoicePosition
        fields = ('product', 'price', 'price', 'quantity',)

    def to_representation(self, instance):
        """Transform Product ID to full Product object for representation"""
        dict_ = super().to_representation(instance)
        dict_.update({
            'product': ProductSerializer(
                Product.objects.get(id=dict_['product'])
            ).data
        })
        return(dict_)
