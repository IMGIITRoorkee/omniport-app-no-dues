import swapper

from no_dues.models import Authority, Subscriber, Permission

Department = swapper.load_model('kernel', 'Department')
common_slugs = ['lib', 'ccb', 'hbc', 'icc', 'iso', 'dor', 'hec', 'acad', 'fin']
ug_slugs = ['nss', 'ncc', 'hoc']
pg_slugs = []


subscribers = Subscriber.objects.all()
authorities = Authority.objects.all()


def generate_permission(authority_slug, subscriber):
    student = subscriber.person.student

    try:
        authority = Authority.objects.get(slug=authority_slug)
        permission, _ = Permission.objects.get_or_create(
            subscriber=subscriber, authority=authority)
    except Exception as e:
        print(f'{student.enrolment_number}: {authority_slug} {str(e)}')


def generate_permissions_for_subscribers(subscribers):
    for subscriber in subscribers:
        student = subscriber.person.student
        department = student.branch.department
        department_code = department.code
        if type(department) is Department:
            slug = '_department'
        else:
            slug = '_centre'

        authority_department_slug = f'{department_code}{slug}'

        slugs = list()
        slugs.append(authority_department_slug)
        slugs.extend(common_slugs)

        graduation_code = student.branch.degree.graduation[0]
        if graduation_code == 'gra':
            slugs.extend(ug_slugs)
        elif graduation_code == 'doc':
            slugs.extend(pg_slugs)

        for slug in slugs:
            generate_permission(slug, subscriber)
