from rest_framework.permissions import BasePermission, SAFE_METHODS

from no_dues.models import Verifier


def has_verifier_rights(person):
    """
    Check if the person is verifier
    :param person: the person whose rights are being checked
    :return: True if the user has privileges, False otherwise
    """

    try:
        verifier = Verifier.objects.get(
            person=person
        )

        return True
    except Verifier.DoesNotExist:
        pass

    return False


def has_verification_rights_on_authority(person, authority):
    """
    Check if the person has rights to verify the authority
    :param person: the person whose rights are being checked
    :param authority: the authority whose verifier the person must be
    :return: True if the user has privileges, False otherwise
    """

    try:
        verifier = Verifier.objects.get(
            person=person,
            authority=authority
        )

        return True
    except Verifier.DoesNotExist:
        pass

    return False


class HasVerifierRights(BasePermission):
    """
    Allow access only to verifiers
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
            and has_verifier_rights(request.person)
        )

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting person has permission to access a Permission
        instance
        :param request: the request being checked for permissions
        :param view: the view to which the request was made
        :param obj: the instance being accessed
        :return: True if safe method or person has rights, False otherwise
        """

        if request.method in SAFE_METHODS:
            return True

        person = request.person
        authority = obj.authority
        return has_verification_rights_on_authority(person, authority)
