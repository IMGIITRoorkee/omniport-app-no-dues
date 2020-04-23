from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from comments.views import CommentViewSet
from no_dues.models import Permission
from no_dues.permissions import (
    has_verification_rights_on_authority, has_subscriber_rights,
    HasSubscriberRights, HasVerifierRights
)


class PermissionCommentViewSet(CommentViewSet):
    """
    The view for CRUD operations of a Permission comment
    """

    permission_classes = [HasSubscriberRights | HasVerifierRights]
    http_method_names = [
        'post',
        'options',
        'head',
    ]

    def create(self, request, *args, **kwargs):
        """
        This function overrides the default create function to create a comment
        and then associate it with the given permission id
        :param request: the request from the client
        :param args: args
        :param kwargs: kwargs
        :return: corresponding response and status code
        """

        try:
            permission_id = request.data.pop('permission_id')
        except KeyError:
            return Response(
                data={
                    'Error': 'Missing permission_id attribute.'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        person = request.user.person
        try:
            permission = Permission.objects.get(id=permission_id)
        except Permission.DoesNotExist():
            return Response(
                data={
                    'Error': 'Requested resource does not exist.'
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        if has_verification_rights_on_authority(person, permission.authority) \
                or permission.subscriber.person == person:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            comment = serializer.save(commenter=person)
            permission.comments.add(comment)
            permission.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                data={
                    'Error': 'You cannot perform this operation.'
                },
                status=status.HTTP_403_FORBIDDEN,
            )
