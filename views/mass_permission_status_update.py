from rest_framework.status import (
    HTTP_403_FORBIDDEN, HTTP_202_ACCEPTED
)
from rest_framework.response import Response
from rest_framework.views import APIView

from kernel.managers.get_role import get_role
from no_dues.constants import (
    APPROVED, NOT_APPLICABLE
)
from no_dues.models import Subscriber, Verifier, Permission
from no_dues.permissions import (
    HasVerifierRights
)


class MassPermissionStatusUpdate(APIView):
    """
    View to update the permission status
    """

    permission_classes = [HasVerifierRights, ]

    def post(self, request):
        person = request.person
        verifier = get_role(person, 'no_dues.Verifier',
                            silent=True, is_custom_role=True)
        authority = verifier.authority
        enrolment_numbers = request.data.get('enrolment_numbers', [])
        status = request.data.get('status', '')

        if status not in [APPROVED, NOT_APPLICABLE]:
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
            permission.save()
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
