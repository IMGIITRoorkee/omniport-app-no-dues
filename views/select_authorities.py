import logging

from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework.views import APIView

from kernel.managers.get_role import get_role
from no_dues.constants import RESIDENCES_EDITED_SLUG, MESS_EDITED_SLUG
from no_dues.models import Permission, Authority
from no_dues.serializers.subscriber import SubscriberSerializer
from no_dues.permissions import (
    IsSubscriber, HasSubscriberRights
)

logger = logging.getLogger('no_dues.views.select_authorities')

class SelectAuthorities(APIView):
    """
    View to select special authorities by the students themselves
    """

    permission_classes = [IsSubscriber & ~HasSubscriberRights]

    def options(self, request):
        residence_options = [{'slug': pair[0], 'name': pair[1]}
                             for pair in RESIDENCES_EDITED_SLUG]
        mess_options = [{'slug': pair[0], 'name': pair[1]}
                             for pair in MESS_EDITED_SLUG]
        logger.info(f'{request.user.username} requested for authorities options')
        return Response(
            data={
                'residence_options': residence_options,
                'mess_options': mess_options
            },
            status=HTTP_200_OK
        )

    def post(self, request):
        person = request.person
        subscriber = get_role(person, 'no_dues.Subscriber',
                              silent=True, is_custom_role=True)
        residences = request.data.get('residences', [])
        mess = request.data.get('mess', '')
        logger.info(f'{request.user.username} requested to select authorities')

        if not residences:
            logger.warn(f'{request.user.username} put a wrong format for residence')
            return Response(
                data={
                    'Error': 'Bad format for the required argument residences.'
                }, status=HTTP_400_BAD_REQUEST,
            )

        for residence in residences:
            if not [item for item in RESIDENCES_EDITED_SLUG if f'{item[0]}' == residence]:
                logger.warn(f'{request.user.username} put a wrong key for residence')
                return Response(
                    data={
                        'Error': f'{residence} key not matched.'
                    }, status=HTTP_400_BAD_REQUEST,
                )
        
        if mess and not [item for item in MESS_EDITED_SLUG if f'{item[0]}' == mess]:
                logger.warn(f'{request.user.username} put a wrong key for mess')
                return Response(
                    data={
                        'Error': f'{mess} key not matched.'
                    }, status=HTTP_400_BAD_REQUEST,
                )

        for residence in residences:
            authority = Authority.objects.get(slug=residence)
            permission, _ = Permission.objects.get_or_create(
                subscriber=subscriber,
                authority=authority,
            )
        
        if mess:
            authority = Authority.objects.get(slug=mess)
            permission, _ = Permission.objects.get_or_create(
                subscriber=subscriber,
                authority=authority,
            )

        subscriber.required_authorities_selected = True
        subscriber.save()
        logger.info(f'{request.user.username} successfully set the residence and mess')

        return Response(
            data=SubscriberSerializer(subscriber).data,
            status=HTTP_201_CREATED,
        )
