import logging
import datetime

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from kernel.managers.get_role import get_role
from no_dues.models import Permission
from no_dues.permissions import (
    HasSubscriberRights, HasVerifierRights, has_subscriber_rights, has_verifier_rights
)
from no_dues.serializers.permission import (
    PermissionListSerializer, PermissionDetailSerializer
)
from no_dues.filters.permission import PermissionFilterSet
from no_dues.pagination.pagination import StudentsPageNumberPagination
from no_dues.utils.log_status_update import log_status_update
from no_dues.utils.send_status_change_notification import (
    send_status_change_notification
)
from no_dues.constants import (
    NOT_REQUESTED,
    REQUESTED,
)

logger = logging.getLogger('no_dues.views.permission')

class PermissionViewset(ModelViewSet):
    """
    The view for CRUD operations of a permission
    """

    serializer_class = PermissionListSerializer
    permission_classes = [HasSubscriberRights | HasVerifierRights]
    http_method_names = [
        'get',
        'patch',
        'options',
        'head',
    ]
    pagination_class = StudentsPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PermissionFilterSet
    search_fields = ['subscriber__person__student__enrolment_number']

    def get_serializer_class(self):
        """
        This function decides the serializer class according to the type of
        request
        :return: the serializer class
        """

        if self.action == 'list':
            return PermissionListSerializer
        elif self.action == 'retrieve':
            return PermissionDetailSerializer
        return PermissionListSerializer

    def get_queryset(self):
        """
        This function overrides the default get_queryset function and displays
        all the apt permissiond to the verifiers (who have verification rights).
        Other users are displayed a list of their asked permissions.
        :return: the corresponding queryset to the view accordingly
        """

        result = []
        person = self.request.person
        if has_subscriber_rights(person):
            logger.info(f'{person.user.username} get its permission list')
            result = Permission.objects.filter(
                subscriber__person=person).order_by('authority')
        elif has_verifier_rights(person):
            logger.info(f'{person.user.username} gets all the no dues for its authority')
            verifier = get_role(person, 'no_dues.Verifier',
                                silent=True, is_custom_role=True)
            result = Permission.objects.filter(
                Q(authority=verifier.authority) &
                ~(Q(status=NOT_REQUESTED))
            ).order_by("-datetime_modified")
            
            data = self.request.query_params
            if data.get('start') is not None and data.get('end') is not None:
                start_date, end_date = data.get('start'), data.get('end')

                start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
                end_date = datetime.datetime.combine(end_date, datetime.time.max)
                result = result.filter(datetime_modified__range=(
                    start_date,
                    end_date
                ))

        return result

    def partial_update(self, request, *args, **kwargs):
        """
        This function overrides the partial_update function (invoked when PATCH
        request is made). This determines the fields that are not editable by
        normal users which can be edited by Verifiers.
        :param request: the request from the client
        :param args: other args
        :param kwargs: other kwargs
        :return: 403 (Forbidden) if the user is not authorized and
        partial_update if user is allowed to perform the same
        """

        person = request.person
        instance = self.get_object()
        request_keys = request.data.keys()
        if 'status' not in request_keys:
            logger.warn(f'{person.user.username} tried to change the status in wrong format')
            return Response(
                data={
                    'Error': 'Missing required argument status.'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if has_subscriber_rights(person) and \
                (instance.status != NOT_REQUESTED or
                 request.data['status'] != REQUESTED):
            logger.warn(f'{person.user.username} tried to change its no dues status which is not allowed')
            return Response(
                data={
                    'Error': 'You cannot perform this operation.'
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        elif has_verifier_rights(request.person) and \
                (request.data['status'] in [NOT_REQUESTED, REQUESTED] or
                 instance.status in [NOT_REQUESTED]):
            logger.warn(f'{person.user.username} tried to change the status of a subscriber which is not allowed')
            return Response(
                data={
                    'Error': 'You cannot perform this operation.'
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        logger.info(f'{person.user.username} changed the status of the permission object')
        return super(PermissionViewset, self).partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        """
        This function overrides the perform_update function (invoked when PATCH
        request is made). This handles the instance after it is updated.
        """

        person = self.request.person
        full_name = person.full_name
        serializer.save()

        instance = self.get_object()
        status_display_name = instance.get_status_display()
        verifier = get_role(person, 'no_dues.Verifier',
                            silent=True, is_custom_role=True)
        if verifier:
            instance.last_modified_by = full_name
            instance.save()
            send_status_change_notification(instance)

        # Add log for status update in form of a comment
        comment = log_status_update(status_display_name, person)
        instance.comments.add(comment)
        instance.save()
