import swapper

from datetime import datetime
from no_dues.models import Subscriber

from no_dues.scripts.generate_permissions import generate_permissions_for_subscribers

from base_auth.managers.get_user import get_user

def create_subscriber(data: dict):

    enrolment_number = data.get('enrolment_number', None)

    if enrolment_number is None:
        return "Please enter an enrolment number", 400
    try:
        person = get_user(enrolment_number).person
    except:
        return "User Doesn't exist", 400

    try:
        subscriber = Subscriber.objects.create(person=person, start_date=datetime.now())
    except:
        return "Error adding No Dues app", 417
    
    generate_permissions_for_subscribers([subscriber])
    return "No Dues app added successfully", 200
