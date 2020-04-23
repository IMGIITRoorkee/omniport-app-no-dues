import swapper
from django.db import models

from kernel.models.roles.base import AbstractRole
from no_dues.models import Authority


class Verifier(AbstractRole):
    """
    This model holds information for the verifiers who have 
    permission on behalf of an authority
    """

    authority = models.ForeignKey(
        to=Authority,
        on_delete=models.CASCADE,
        related_name='verifiers',
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        authority = self.authority
        person = self.person

        return f'{authority}: {person}'
