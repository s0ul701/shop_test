from django.core.validators import MinValueValidator
from django.db import models


from apps.utils import get_file_path


class Product(models.Model):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=(MinValueValidator(0),),
        verbose_name='Price, $',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Quantity, pices',
    )
    image = models.ImageField(
        upload_to=get_file_path,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
