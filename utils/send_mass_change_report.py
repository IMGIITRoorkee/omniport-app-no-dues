from django.conf import settings
from emails.actions import email_push

from categories.models import Category


def send_mass_change_report(report, verifier, update):
    """
    :param report: Mass update report
    :param verifier: Verifier object
    :param update: Update status
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

    authority = verifier.authority
    person = verifier.person
    full_name = person.full_name
    persons = list(authority.verifiers.values_list(
        'person_id', flat=True).distinct())

    full_path = f'https://newchanneli.iitr.ac.in/?next=/no_dues'
    subject_text = 'Mass update report'

    body_text = """Hello,
    The following is the mass update report updated by {} to the status {}.
    <br><br>
    <table style="border: 1px solid black">
    <tr style="border: 1px solid black">
        <th style="border: 1px solid black">Enrolment Number</th>
        <th style="border: 1px solid black">Status (0-Fail, 1-Success)</th>
        <th style="border: 1px solid black">Description</th>
    </tr>
    """
    body_text = body_text.format(full_name, update)
    table_row_text = """<tr style="border: 1px solid black">
        <td style="border: 1px solid black">{}</td>
        <td style="border: 1px solid black">{}</td>
        <td style="border: 1px solid black">{}</td>
    """

    for record in report:
        body_text = body_text + \
            table_row_text.format(
                record['enrolment_number'], record['Status'], record['Info'])

    body_text = body_text + '</table>'

    try:
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
