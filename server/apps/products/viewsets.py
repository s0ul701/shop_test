from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAdminUser

from apps.products.models import Product
from apps.products.permissions import ReadOnly
from apps.products.serializers import ProductSerializer


class ProductViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAdminUser | ReadOnly,)
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ('deal_date', 'price', 'quantity', )
    search_fields = ('title', 'description',)
