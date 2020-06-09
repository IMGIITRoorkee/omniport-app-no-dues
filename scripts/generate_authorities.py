from no_dues.constants import (
    DEPARTMENTS_EDITED_SLUG, CENTRES_EDITED_SLUG, RESIDENCES_EDITED_SLUG, 
    MESS_EDITED_SLUG, CLUBS, OTHER_AUTHORITIES
)
from no_dues.models import Authority


def generate_authorities(authorities):
    for authority in authorities:
        Authority.objects.get_or_create(
            slug=f'{authority[0]}',
            full_name=authority[1].strip()
        )


def generate_department_authorities():
    generate_authorities(DEPARTMENTS_EDITED_SLUG)


def generate_centre_authorities():
    generate_authorities(CENTRES_EDITED_SLUG)


def generate_residence_authorities():
    generate_authorities(RESIDENCES_EDITED_SLUG)

def generate_mess_authorities():
    generate_authorities(MESS_EDITED_SLUG)

def generate_club_authorities():
    generate_authorities(CLUBS)

def generate_other_authorities():
    generate_authorities(OTHER_AUTHORITIES)
