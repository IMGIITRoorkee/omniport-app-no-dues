import swapper
from django.db import models

from kernel.managers.get_role import get_role
from formula_one.models.base import Model
from comments.mixins import CommentableMixin
from no_dues.models import Subscriber, Authority
from no_dues.constants import (
    PERMISSION_STATUSES, NOT_REQUESTED
)


class Permission(CommentableMixin, Model):
    """
    This model holds information for about a permission 
    asked by a subscriber to an authority
    """

    subscriber = models.ForeignKey(
        to=Subscriber,
        on_delete=models.CASCADE,
        related_name='permissions',
    )
    authority = models.ForeignKey(
        to=Authority,
        on_delete=models.CASCADE,
        related_name='permissions',
    )
    status = models.CharField(
        max_length=3,
        choices=PERMISSION_STATUSES,
        default=NOT_REQUESTED,
    )
    last_modified_by = models.CharField(
        max_length=127,
        blank=True,
        null=True,
    )

    class Meta:
        """
        Meta class for Permission
        """

        unique_together = ('subscriber', 'authority')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        subscriber = self.subscriber
        authority = self.authority
        status = self.status

        return f'{authority}: {subscriber} ({status})'

    @property
    def latest_comment_by(self):
        """
        Return if the last comment was by a subscriber or verifier
        :return: the string to represent if the latest comment by a 
        subscriber or verifier
        """

        latest_comment = self.comments.last()
        if latest_comment is not None:
            commenter = latest_comment.commenter
            return 'verifier' if get_role(commenter, 'no_dues.Verifier',
                                          silent=True, is_custom_role=True) \
                is not None else 'subscriber'

        return ''
