from no_dues.utils.send_notification import send_notification


no_due_text = """
Hey {},
<br /><br />
All of your no dues are either marked Approved, Not Applicable or Approved on Condition.
You have obtained the no dues slip from all of the required departments/sections. The
Academic section has been intimated. All the further process will be handled by the Academic
section itself.
"""


def send_status_change_notification(permission):
    """
    :param permission: Permission instance whose status is changed
    :return:
    """

    front_path = 'no_dues/'

    status_display = permission.get_status_display()
    authority_full_name = permission.authority.full_name
    subscriber = permission.subscriber
    no_due = subscriber.no_due

    subject_text = f'{authority_full_name} has marked your no dues to {status_display}'
    body_text = f'{authority_full_name} has changed the status of your no dues to {status_display}.'

    send_notification(subject_text, body_text,
                      front_path, False, subscriber, None)

    if no_due:
        subject_text = 'Congratulations! You have obtained all the required no dues.'
        send_notification(
            subject_text, no_due_text.format(subscriber.person.full_name),
            front_path, False, subscriber, None
        )
