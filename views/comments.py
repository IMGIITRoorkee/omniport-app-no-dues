from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from comments.views import CommentViewSet
from no_dues.models import Permission
from no_dues.permissions import (
    has_verification_rights_on_authority, has_subscriber_rights,
    HasSubscriberRights, HasVerifierRights
)
from no_dues.utils.log_status_update import log_status_update
from no_dues.utils.send_comment_notification import (
    send_comment_notification
)
from no_dues.constants import REPORTED


class PermissionCommentViewSet(CommentViewSet):
    """
    The view for CRUD operations of a Permission comment
    """

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
            permission_id = request.data.pop('permission_id')[0]
            mark_reported = request.data.get('mark_reported', [False])[0]
            person = request.person
            permission = Permission.objects.get(id=permission_id)
            is_right_authority = has_verification_rights_on_authority(
                person, permission.authority
            )
            if is_right_authority or permission.subscriber.person == person:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                comment = serializer.save(commenter=person)

                if is_right_authority and mark_reported:
                    full_name = person.full_name
                    permission.status = REPORTED
                    permission.last_modified_by = full_name
                    status_display_name = permission.get_status_display()

                    # Add log for status update in form of a comment
                    status_comment = log_status_update(
                        status_display_name, person)
                    permission.comments.add(status_comment)

                permission.comments.add(comment)
                permission.save()
                send_comment_notification(
                    permission, comment, is_right_authority)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    data={
                        'Error': 'You cannot perform this operation.'
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

        except KeyError:
            return Response(
                data={
                    'Error': 'Missing permission_id attribute.'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Permission.DoesNotExist:
            return Response(
                data={
                    'Error': 'Requested resource does not exist.'
                },
                status=status.HTTP_404_NOT_FOUND,
            )
