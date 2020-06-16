from django.contrib.auth.models import User
from django.db import models


class Invoice(models.Model):
    customer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='invoices',
    )
    deal_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Invoice #{self.id}'

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
