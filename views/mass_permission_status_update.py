from rest_framework.status import (
    HTTP_403_FORBIDDEN, HTTP_202_ACCEPTED
)
from rest_framework.response import Response
from rest_framework.views import APIView

from kernel.managers.get_role import get_role
from no_dues.constants import (
    REPORTED, APPROVED, NOT_APPLICABLE
)
from no_dues.models import Subscriber, Verifier, Permission
from no_dues.permissions import (
    HasVerifierRights
)
from no_dues.utils.log_status_update import log_status_update
from no_dues.utils.send_status_change_notification import (
    send_status_change_notification
)


class MassPermissionStatusUpdate(APIView):
    """
    View to update the permission status
    """

    permission_classes = [HasVerifierRights, ]

    def post(self, request):
        person = request.person
        full_name = person.full_name
        verifier = get_role(person, 'no_dues.Verifier',
                            silent=True, is_custom_role=True)
        authority = verifier.authority
        enrolment_numbers = request.data.get('enrolment_numbers', [])
        status = request.data.get('status', '')

        if status not in [APPROVED, NOT_APPLICABLE, REPORTED]:
            return Response(
                data={
                    'Error': 'You cannot perform this operation.'
                }, status=HTTP_403_FORBIDDEN,
            )

        report = list()
        for enrolment_number in enrolment_numbers:
            report_entity = dict()
            try:
                subscriber = Subscriber.objects.get(
                    person__student__enrolment_number=enrolment_number)
            except Exception as e:
                report_entity['Status'] = 0
                report_entity['Info'] = str(e)
                report.append(report_entity)
                continue
            try:
                permission, _ = Permission.objects.get_or_create(
                    subscriber=subscriber,
                    authority=authority
                )
            except Exception as e:
                report_entity['Status'] = 0
                report_entity['Info'] = str(e)
                report.append(report_entity)
                continue
            permission.status = status
            permission.last_modified_by = full_name

            # Add log for status update in form of a comment
            status_display_name = permission.get_status_display()
            comment = log_status_update(status_display_name, person)
            permission.comments.add(comment)

            permission.save()

            send_status_change_notification(permission)
            report_entity['Status'] = 1
            report_entity['Info'] = 'Success'
            report.append(report_entity)

        total = len(report)
        success = sum([report_entity['Status'] for report_entity in report])
        failed = total - success
        return Response(
            data={
                'total': total,
                'success': success,
                'failed': failed
            },
            status=HTTP_202_ACCEPTED,
        )
