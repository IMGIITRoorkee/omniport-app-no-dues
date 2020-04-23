from django.conf import settings

settings.ROLES.extend([
    'no_dues.Subscriber',
    'no_dues.Verifier'
])
