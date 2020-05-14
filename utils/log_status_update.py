from datetime import datetime

from comments.models import Comment


def log_status_update(status_display_name, commenter):
    """
    :param status_display_name: New status display name
    :param commenter: The commenter who updated the status
    :return: A new comment instance
    """
    now = datetime.now()
    datetime_string = now.strftime("at %H:%M:%S hrs on %-d %b, %Y")

    full_name = commenter.full_name

    text = f'Status changed to {status_display_name} by {full_name} {datetime_string}'

    comment = Comment()
    comment.text = text
    comment.commenter = commenter
    comment.save()

    return comment
