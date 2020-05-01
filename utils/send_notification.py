from django.conf import settings
from notifications.actions import push_notification
from emails.actions import email_push

from categories.models import Category


def send_notification(subject_text, body_text, front_path, to_authority, subscriber, authority):
    """
    :param subject_text: Subject text for the email
    :param body_text: Body text for the email
    :param front_path: Path to the redirection view after the host
    :param to_authority: If the notification is for authority
    :param subscriber: Subscriber object
    :param authority: Authority object
    :return:
    """

    app = settings.DISCOVERY.get_app_configuration(
        'no_dues'
    )
    app_verbose_name = app.nomenclature.verbose_name
    app_slug = app.nomenclature.name

    category, _ = Category.objects.get_or_create(
        name=app_verbose_name,
        slug=app_slug,
    )

    if to_authority and authority is None:
        raise Exception(
            'to_authority and authority parameter can not be False together'
        )
    elif subscriber is None:
        raise Exception(
            'Can not set subscriber to None with to_authority marked as False'
        )

    if to_authority:
        persons = list(authority.verifiers.values_list(
            'person_id', flat=True).distinct())
    else:
        subscriber_person_id = subscriber.person_id
        persons = list()
        persons.append(subscriber_person_id)

    full_path = f'https://newchanneli.iitr.ac.in/?next=/{front_path}'

    try:
        push_notification(
            template=subject_text,
            category=category,
            web_onclick_url=front_path,
            android_onclick_activity='',
            ios_onclick_action='',
            is_personalised=False,
            person=None,
            has_custom_users_target=True,
            persons=persons,
        )

        email_push(
            subject_text=subject_text,
            body_text=body_text,
            category=category,
            has_custom_user_target=True,
            persons=persons,
            target_app_name=app_verbose_name,
            target_app_url=full_path,
        )

    except Exception as e:
        pass
