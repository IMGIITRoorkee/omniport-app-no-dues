import swapper

from django.core.exceptions import ObjectDoesNotExist

from base_auth.managers.get_user import get_user
from kernel.managers.get_role import get_role

from no_dues.models import Subscriber, Authority, Permission


Student = swapper.load_model('kernel', 'Student')

def create_subscriber_permission(data: dict):
    student_id = data.get("student_id", None)
    authority_id = data.get("no_dues_authority", None)

    if not (student_id and authority_id):
        return "Insufficient data", 400

    try:
        person = get_user(student_id).person
    except:
        return f"Cannot find student: {student_id}", 404
    else:
        if get_role(person=person, role_name='Student', silent=True) is None:
            return f"Not a student: {student_id}", 400

        try:
            subscriber = Subscriber.objects.get(person=person)
        except ObjectDoesNotExist:
            return f"Cannot find subscriber for student: {student_id}", 404
        except:
            return f"Error fetching subscriber: {student_id}", 404
        else:
            authority = Authority.objects.get(id=authority_id)

            try:
                permission = Permission.objects.get(subscriber=subscriber, authority=authority)
            except ObjectDoesNotExist:
                permission = Permission(subscriber=subscriber, authority=authority)
                try:
                    permission.save()
                except:
                    return "Error creating permission", 417
                else:
                    return f"Permission created successfully for student: {student_id}, and authority: {authority_id}", 201
            else:
                return f"Permission already exists for student: {student_id}, and authority: {authority_id}", 400

