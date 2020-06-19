from rest_framework import serializers

from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for create/retrieve/list/update Products"""
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'image',)
