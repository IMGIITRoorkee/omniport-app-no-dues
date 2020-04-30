from no_dues.utils.send_notification import send_notification


def send_comment_notification(permission, comment, by_authority):
    """
    :param permission: Permission instance where the new comment is added
    :param comment: Comment instance
    :param by_authority: If the commenter is an authority
    :return:
    """

    authority = permission.authority
    subscriber = permission.subscriber
    authority_full_name = authority.full_name
    subscriber_full_name = subscriber.person.full_name

    commenter_full_name = authority_full_name if by_authority else subscriber_full_name
    relation_word = 'your' if by_authority else 'his'

    subject_text = f'You have a new comment by {commenter_full_name}'
    body_text = f'{commenter_full_name} added a comment on {relation_word} no due: '
    body_text = body_text + comment.text

    front_path = f'no_dues/permission/{permission.id}/'
    to_authority = not by_authority

    send_notification(subject_text, body_text,
                      front_path, to_authority, subscriber, authority)
