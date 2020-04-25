import swapper
from rest_framework import serializers

from formula_one.serializers.base import ModelSerializer
from kernel.serializers.person import AvatarSerializer
from no_dues.models import Subscriber


class SubscriberSerializer(ModelSerializer):
    """
    Serializer for the Subscriber model
    """

    person = AvatarSerializer(
        read_only=True,
    )

    no_due = serializers.BooleanField(
        read_only=True,
    )

    required_authorities_selected = serializers.BooleanField(
        read_only=True,
    )

    class Meta:
        """
        Meta class for SubscriberSerializer
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
            'required_authorities_selected',
        ]
