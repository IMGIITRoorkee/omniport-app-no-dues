from rest_framework.permissions import BasePermission

from no_dues.models import Subscriber


def is_subscriber(person):
    """
    Check if the person is a subscriber
    :param person: the person whose rights are being checked
    :return: True if the user has privileges, False otherwise
    """

    try:
        subscriber = Subscriber.objects.get(
            person=person
        )

        return True
    except Subscriber.DoesNotExist:
        pass

    return False


def has_subscriber_rights(person):
    """
    Check if the person is a subscriber and has uploaded the ID card and 
    selected their required authorities
    :param person: the person whose rights are being checked
    :return: True if the user has privileges, False otherwise
    """

    try:
        subscriber = Subscriber.objects.get(
            person=person
        )

        return bool(subscriber.id_card) and \
            subscriber.required_authorities_selected
    except Subscriber.DoesNotExist:
        pass

    return False


class IsSubscriber(BasePermission):
    """
    Allow access only to subscribers
    """

    def has_permission(self, request, view):
        """
        Check if the requesting person has permission to access the view
        :param request: the request being checked for permissions
        :param view: the view to which the request was made
        :return: True if safe method or person has rights, False otherwise
        """
        return(
            request.user is not None
            and request.person is not None
            and is_subscriber(request.person)
        )


class HasSubscriberRights(BasePermission):
    """
    Allow access only to subscribers
    """

    def has_permission(self, request, view):
        """
        Check if the requesting person has permission to access the view
        :param request: the request being checked for permissions
        :param view: the view to which the request was made
        :return: True if safe method or person has rights, False otherwise
        """
        return(
            request.user is not None
            and request.person is not None
            and has_subscriber_rights(request.person)
        )

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting person has permission to access a Permission
        instance
        :param request: the request being checked for permissions
        :param view: the view to which the request was made
        :param obj: the instance being accessed
        :return: True if person is the subscriber of the permission, False otherwise
        """

        person = request.person
        subscriber_person = obj.subscriber.person
        return person == subscriber_person
