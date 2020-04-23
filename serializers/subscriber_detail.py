import swapper
from rest_framework import serializers

from formula_one.serializers.base import ModelSerializer
from kernel.serializers.person import AvatarSerializer
from no_dues.models import Subscriber
from no_dues.serializers.permission import PermissionBaseSerializer
from no_dues.serializers.subscriber import SubscriberSerializer


class SubscriberDetailSerializer(SubscriberSerializer):
    """
    Serializer for the detail Subscriber model
    """

    permissions = PermissionBaseSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        """
        Meta class for SubscriberDetailSerializer
        """

        model = Subscriber
        exclude = [
            'datetime_created',
            'datetime_modified',
            'start_date',
            'end_date',
        ]
        read_only = [
            'person',
            'no_due',
            'permissions',
        ]
