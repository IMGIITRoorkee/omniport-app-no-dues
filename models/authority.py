import swapper
from django.db import models

from formula_one.models.base import Model


class Authority(Model):
    """
    This model holds information for the various authorisation groups
    """

    slug = models.SlugField(
        max_length=127,
        unique=True,
    )

    full_name = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    class Meta:
        """
        Meta class for Authority
        """

        verbose_name_plural = 'Authorities'

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        slug = self.slug
        full_name = self.full_name

        return f'{slug}: {full_name}'
