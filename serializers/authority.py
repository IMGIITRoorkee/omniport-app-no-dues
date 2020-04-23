import swapper
from rest_framework import serializers

from formula_one.serializers.base import ModelSerializer
from no_dues.models import Authority


class AuthoritySerializer(ModelSerializer):
    """
    Serializer for the Authority model
    """

    class Meta:
        """
        Meta class for AuthoritySerializer
        """

        model = Authority
        exclude = [
            'datetime_created',
            'datetime_modified',
        ]
        depth = 1
