from no_dues.models import *


from base_auth.managers.get_user import get_user
from django.db.models import Q

def get_sub(enrolment_number):

    return Subscriber.objects.get(person=get_user(enrolment_number).person)


def get_perm(sub, term):

    auth = Authority.objects.get(full_name__contains=term)

    return Permission.objects.get(authority=auth, subscriber=sub)


def set_perm(perm, status, last_mod):
    perm.status=status
    perm.last_modified_by = last_mod

    perm.save()


