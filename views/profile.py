import logging

from rest_framework.generics import RetrieveUpdateAPIView

from kernel.managers.get_role import get_role
from no_dues.models import Subscriber, Verifier
from no_dues.permissions import (
    is_subscriber, has_verifier_rights, HasVerifierRights, IsSubscriber
)
from no_dues.serializers.subscriber import SubscriberSerializer
from no_dues.serializers.verifier import VerifierSerializer

logger = logging.getLogger('no_dues.views.profile')

class ProfileView(RetrieveUpdateAPIView):
    """
    The view for the profile
    """

    permission_classes = [IsSubscriber | HasVerifierRights]
    serializer_class = SubscriberSerializer

    def get_serializer_class(self):
        """
        This function decides the serializer class according to the type of
        request
        :return: the serializer class
        """

        person = self.request.person
        if is_subscriber(person):
            return SubscriberSerializer
        elif has_verifier_rights(person):
            return VerifierSerializer
        return SubscriberSerializer

    def get_object(self):
        """
        Handles the object instance for displaying
        """

        person = self.request.person
        instance = None
        if is_subscriber(person):
            logger.info(f'{person.user.username} requested profile information as subscriber')
            instance = get_role(person, 'no_dues.Subscriber',
                                silent=True, is_custom_role=True)
        elif has_verifier_rights(person):
            logger.info(f'{person.user.username} requested profile information as verifier')
            instance = get_role(person, 'no_dues.Verifier',
                                silent=True, is_custom_role=True)

        return instance
