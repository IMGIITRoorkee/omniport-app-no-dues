import logging

from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from kernel.managers.get_role import get_role
from no_dues.serializers.subscriber import SubscriberSerializer
from no_dues.permissions import (
    IsSubscriber, HasSubscriberRights
)

logger = logging.getLogger('no_dues.views.select_authorities')

class AddAuthorities(APIView):
    """
    View to make the student eligible to add special authorities by themselves
    """
    permission_classes = [IsSubscriber & HasSubscriberRights]

    def post(self, request):
        person = request.person
        subscriber = get_role(person, 'no_dues.Subscriber',
                              silent=True, is_custom_role=True)
        if not subscriber:
            logger.warn(f'{request.user.username} tried to change authorities without being a subscriber')
            return Response(
                data={
                    'Error': 'You are not a subscriber.'
                }, status=HTTP_400_BAD_REQUEST,
            )
        logger.info(f'{request.user.username} requested to be eligible to add authorities')

        subscriber.required_authorities_selected = False
        subscriber.save()
        logger.info(f'{request.user.username} successfully made subscriber eligible to add authorities')
        return Response(
            data=SubscriberSerializer(subscriber).data,
            status=HTTP_200_OK,
        )
