import swapper
from rest_framework import serializers

from formula_one.serializers.base import ModelSerializer
from kernel.serializers.person import AvatarSerializer
from no_dues.models import Verifier
from no_dues.serializers.authority import AuthoritySerializer


class VerifierSerializer(ModelSerializer):
    """
    Serializer for the Verifier model
    """

    person_name = serializers.CharField(
        source='person.full_name',
        read_only=True,
    )

    authority = AuthoritySerializer(
        read_only=True,
    )

    class Meta:
        """
        Meta class for VerifierSerializer
        """

        model = Verifier
        exclude = [
            'datetime_created',
            'datetime_modified',
            'start_date',
            'end_date',
        ]
        read_only = '__all__'
