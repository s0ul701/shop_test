from django.core.validators import MinValueValidator
from django.db import models


class InvoicePosition(models.Model):
    product = models.ForeignKey(
        to='products.Product',
        on_delete=models.CASCADE,
        related_name='invoice_positions',
    )
    invoice = models.ForeignKey(
        to='invoices.Invoice',
        on_delete=models.CASCADE,
        related_name='positions',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=(MinValueValidator(0),),
        verbose_name='Price, $',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Quantity, pices',
    )

    def __str__(self):
        return f'{self.product.title}, {self.quantity} * {self.price}$'

    class Meta:
        verbose_name = 'Invoice position'
        verbose_name_plural = 'Invoice positions'
