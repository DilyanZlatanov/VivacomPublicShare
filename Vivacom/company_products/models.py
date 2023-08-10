from django.core.validators import MinLengthValidator
from django.db import models


class CreateProductModel(models.Model):
    MIN_LENGTH = 2
    product_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
        unique=True,

    )

    description = models.TextField(
        max_length=300,
        blank=False,
        null=False,
    )
