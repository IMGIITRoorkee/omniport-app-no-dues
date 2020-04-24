import swapper
from django.db import models
from django.db.models import Q

from kernel.models.roles.base import AbstractRole
from formula_one.utils.upload_to import UploadTo
from no_dues.constants import (
    APPROVED, NOT_APPLICABLE
)


class Subscriber(AbstractRole):
    """
    This model holds information for the subscribers who need to have NOC
    """

    id_card = models.ImageField(
        upload_to=UploadTo('no_dues', 'id_cards'),
        verbose_name='Institute ID card',
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        person = self.person
        student = person.student

        return f'{student}'

    @property
    def no_due(self):
        permissions = self.permissions
        due = permissions.filter(
            ~(Q(status=APPROVED) | Q(status=NOT_APPLICABLE))).exists()
        no_due = not due
        return no_due
