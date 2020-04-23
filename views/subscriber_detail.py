from rest_framework.generics import RetrieveAPIView, get_object_or_404

from no_dues.models import Subscriber, Verifier
from no_dues.permissions import (
    HasVerifierRights
)
from no_dues.serializers.subscriber_detail import SubscriberDetailSerializer


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
