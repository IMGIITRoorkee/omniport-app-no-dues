import swapper
from rest_framework import serializers

from comments.serializers import CommentSerializer
from formula_one.serializers.base import ModelSerializer
from no_dues.models import Permission
from no_dues.serializers.authority import AuthoritySerializer
from no_dues.serializers.subscriber import SubscriberSerializer


class PermissionBaseSerializer(ModelSerializer):
    """
    Base serializer for the Permission model
    """

    authority = AuthoritySerializer(
        read_only=True,
    )
    status_display_name = serializers.CharField(source='get_status_display')

    class Meta:
        """
        Meta class for PermissionListSerializer
        """

        model = Permission
        exclude = [
            'datetime_created',
            'datetime_modified',
            'comments',
            'subscriber',
        ]
        read_only = [
            'id',
            'authority',
            'status_display_name',
        ]


class PermissionListSerializer(PermissionBaseSerializer):
    """
    Serializer for the Permission model
    """

    subscriber = SubscriberSerializer(
        read_only=True,
    )

    class Meta:
        """
        Meta class for PermissionListSerializer
        """

        model = Permission
        exclude = [
            'datetime_created',
            'datetime_modified',
            'comments',
        ]
        read_only = [
            'id',
            'subscriber',
            'authority',
            'status_display_name',
        ]


class PermissionDetailSerializer(PermissionListSerializer):
    """
    Serializer for the detail view of Permission viewset
    """

    comments = CommentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        """
        Meta class for PermissionDetailSerializer
        """

        model = Permission
        exclude = [
            'datetime_created',
            'datetime_modified',
        ]
        read_only = [
            'id',
            'subscriber',
            'authority',
            'status_display_name',
        ]
