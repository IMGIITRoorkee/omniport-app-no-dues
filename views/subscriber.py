import logging

import pandas as pd
from django.db.models import F, Q
from django.http import HttpResponse
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, get_object_or_404
)
from rest_framework import status
from rest_framework.response import Response

from no_dues.models import Subscriber, Verifier, Permission
from no_dues.permissions import (
    HasVerifierRights
)
from no_dues.serializers.subscriber import SubscriberSerializer
from no_dues.serializers.subscriber_detail import SubscriberDetailSerializer
from no_dues.utils.beautify_dataframe import (
    beautify_mass_dataframe, beautify_subscriber_dataframe, delete_extra_columns
)

logger = logging.getLogger('no_dues.views.subscriber')

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
        username = request.user.username
        try:
            download = request.query_params.get('download', '')
            if download == 'xlsx':
                
                logger.info(f'{username} requested for the subscribers data')

                permissions_query = Q(subscriber__id_card='') \
                    | Q(subscriber__person__student__current_semester__gt=F('subscriber__person__student__branch__semester_count'))
                subscribers_query = Q(id_card='') \
                    | Q(person__student__current_semester__gt=F('person__student__branch__semester_count'))
                permissions = Permission.objects.exclude(permissions_query)
                subscribers = Subscriber.objects.exclude(subscribers_query)

                permissions_df = pd.DataFrame(list(permissions.values(
                    'authority__full_name', 'status', 'subscriber__person__student__enrolment_number')))
                subscribers_df = pd.DataFrame(list(subscribers.values( 
                    'person__full_name', 'person__student__enrolment_number', 'person__student__branch__name',
                    'person__student__branch__entity_content_type_id', 'person__student__branch__entity_object_id')))

                subscribers_df = subscribers_df.apply(beautify_subscriber_dataframe, axis=1)
                del subscribers_df['person__student__branch__entity_object_id']
                del subscribers_df['person__student__branch__entity_content_type_id']
                subscribers_df.rename(columns={
                    'person__full_name': 'Name',
                    'person__student__enrolment_number': 'Enrolment No.',
                    'person__student__branch__name': 'Branch'
                }, inplace=True)

                permissions_df=pd.pivot(permissions_df, index='subscriber__person__student__enrolment_number', 
                                        columns='authority__full_name', values='status')
                permissions_df = permissions_df.reset_index()
                permissions_df = pd.merge(permissions_df, subscribers_df, 
                                          how='left', left_on='subscriber__person__student__enrolment_number',
                                          right_on='Enrolment No.')
                permissions_df.rename(columns={
                    'subscriber__person__student__enrolment_number': 'Enrolment No.',
                }, inplace=True)
                permissions_df = permissions_df.fillna('nreq')
                permissions_df = permissions_df.apply(beautify_mass_dataframe, axis=1)
                permissions_df = delete_extra_columns(permissions_df)

                filename = 'Final_year_students.csv'
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename={filename}'
                permissions_df.to_csv(
                    path_or_buf=response, index=False, header=True)

                logger.info(f'{username} successfully get the subscribers data')

                return response

        except KeyError:
            logger.error(f'{username} got a keyerror while getting the subscriber data')

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
        logger.info('f{self.request.user.username} retrieved the details for {enrolment_number}')
        return subscriber
