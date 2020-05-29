from no_dues.utils.send_notification import send_notification


no_due_text = """
<br><br>
All of your no dues are either marked Approved, Not Applicable or Approved on Condiion. 
You are now eligible to obtain the final no dues slip. Log in to the Channel i to check 
the further process.
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

    if no_due:
        body_text = body_text + no_due_text

    send_notification(subject_text, body_text,
                      front_path, False, subscriber, None)
