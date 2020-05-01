import swapper
from rest_framework import serializers

from formula_one.serializers.base import ModelSerializer
from kernel.serializers.person import AvatarSerializer
from no_dues.models import Subscriber


class SubscriberSerializer(ModelSerializer):
    """
    Serializer for the Subscriber model
    """

    person_id = serializers.IntegerField(
        source="person.id",
        read_only=True,
    )

    no_due = serializers.BooleanField(
        read_only=True,
    )

    required_authorities_selected = serializers.BooleanField(
        read_only=True,
    )

    person_name = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )

    person_degree = serializers.CharField(
        source="person.student.branch.degree.name",
        read_only=True,
    )

    person_enrolment = serializers.CharField(
        source='person.student.enrolment_number',
        read_only=True,
    )

    person_department = serializers.CharField(
        source="person.student.branch.name",
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
            'person',
        ]
        read_only = [
            'no_due',
            'required_authorities_selected',
        ]
