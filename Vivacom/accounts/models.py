from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinLengthValidator
from django.db import models


class UserRegistrationModel(models.Model):
    MIN_LENGTH = 2
    username = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    password1 = models.CharField(
        null=False,
        blank=False,
    )

    password2 = models.CharField(
        blank=False,
        null=False,
    )


class UserLoginModel(models.Model):
    username = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
