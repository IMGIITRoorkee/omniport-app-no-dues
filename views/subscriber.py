import pandas as pd
from django.http import HttpResponse
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, get_object_or_404
)
from rest_framework import status
from rest_framework.response import Response

from no_dues.models import Subscriber, Verifier
from no_dues.permissions import (
    HasVerifierRights
)
from no_dues.serializers.subscriber import SubscriberSerializer
from no_dues.serializers.subscriber_detail import SubscriberDetailSerializer


class SubscriberListView(ListAPIView):
    """
    The view for the list of subscribers
    """

    permission_classes = [HasVerifierRights, ]
    serializer_class = SubscriberSerializer
    pagination_class = None

    def get_queryset(self):
        subscribers = [
            subscriber for subscriber in Subscriber.objects.all() if subscriber.no_due]
        return subscribers

    def list(self, request, *args, **kwargs):
        try:
            download = request.query_params.get('download', '')
            if download == 'xlsx':

                subscriber_list = list()
                subscribers = Subscriber.objects.exclude(id_card='')
                for subscriber in subscribers:
                    person = subscriber.person
                    student = person.student
                    enrolment_number = student.enrolment_number
                    name = person.full_name
                    branch_name = student.branch.name
                    department_name = student.branch.department.name
                    no_due = subscriber.no_due

                    subscriber_object = dict()
                    subscriber_object['Enrolment Number'] = enrolment_number
                    subscriber_object['Name'] = name
                    subscriber_object['Branch'] = branch_name
                    subscriber_object['Department'] = department_name
                    subscriber_object['Department Status'] = ''
                    department = 'Not Found'
                    mess = 'No Mess'
                    bhawans = list()
                    for permission in subscriber.permissions.all():
                        authority_slug = permission.authority.slug
                        authority_name = permission.authority.full_name
                        status_display = permission.get_status_display()
                        if '_department' in authority_slug:
                            department = status_display
                        elif '_bhawan' in authority_slug:
                            bhawans.append(f'{authority_name} - {status_display}')
                        elif '_mess' in authority_slug:
                            mess = f'{authority_name} - {status_display}'
                        else:
                            subscriber_object[authority_name] = status_display
                    subscriber_object['Department Status'] = department
                    subscriber_object['Bhawan'] = bhawans
                    subscriber_object['Mess'] = mess
                    subscriber_object['Final Status'] = \
                        'All Approved, Not Applicable or Approved on Condition' if no_due else 'Pending'
                    subscriber_list.append(subscriber_object)

                subscriber_list_df = pd.DataFrame(subscriber_list)
                filename = 'Final_year_students.csv'
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename={filename}'
                subscriber_list_df = subscriber_list_df.fillna('Not Required')
                subscriber_list_df.to_csv(
                    path_or_buf=response, index=False, header=True)
                return response

        except KeyError:
            pass

        return super(SubscriberListView, self).list(self, request, *args, **kwargs)


class SubscriberDetailView(RetrieveAPIView):
    """
    The view for the subsciber details
    """

    permission_classes = [HasVerifierRights, ]
    serializer_class = SubscriberDetailSerializer
    lookup_url_kwarg = 'enrolment_number'

    def get_object(self):
        enrolment_number = self.kwargs.get(self.lookup_url_kwarg)
        subscriber = get_object_or_404(
            Subscriber, person__student__enrolment_number=enrolment_number)
        return subscriber
