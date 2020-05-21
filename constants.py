from shell.constants.residences import RESIDENCES
from shell.constants.departments import DEPARTMENTS
from shell.constants.centres import CENTRES

# Permission statuses
NOT_REQUESTED = 'nrq'
REQUESTED = 'req'
REPORTED = 'rep'
NOT_APPLICABLE = 'nap'
APPROVED = 'app'

PERMISSION_STATUSES = (
    (NOT_REQUESTED, 'Not Requested'),
    (REQUESTED, 'Requested'),
    (REPORTED, 'Reported'),
    (NOT_APPLICABLE, 'Not Applicable'),
    (APPROVED, 'Approved'),
)

# Residences
RESIDENCES_EDITED_SLUG = [(f'{x[0]}_bhawan', x[1].strip()) for x in RESIDENCES]

# Departments
DEPARTMENTS_EDITED_SLUG = [(f'{x[0]}_department', x[1].strip()) for x in DEPARTMENTS]

# Centres
CENTRES_EDITED_SLUG = [(f'{x[0]}_centre', x[1].strip()) for x in CENTRES]

# Clubs
NSS = 'nss'
NCC = 'ncc'
NSO = 'nso'
HEC = 'hec'
HOBBIES_CLUB = 'hoc'

CLUBS = (
    (NSS, 'National Service Scheme'),
    (NCC, 'National Cadet Corps'),
    (NSO, 'National Sports Organisation'),
    (HEC, 'Himalayan Explorer\'s Club'),
    (HOBBIES_CLUB, 'Hobbies Club')
)

# Other authorities
LIBRARY = 'lib'
CCB_OFFICE = 'ccb'
HOSPITAL_BOOKLET_CANCELLATION = 'hbc'
INSTITUTE_COMPUTER_Centre = 'icc'
INSTITUTE_SPORTS_ASSOCIATION = 'iso'
THESIS_SUBMISSION_PROOF = 'tsp'
ALUMNI_MEMBERSHIP_PROOF = 'amp'
BANK_ACCOUNT_DETAILS = 'bad'
FINANCE_SECTION = 'acad'
ACADEMIC_SECTION = 'fin'

OTHER_AUTHORITIES = (
    (LIBRARY, 'Central Library'),
    (CCB_OFFICE, 'CCB Office'),
    (INSTITUTE_COMPUTER_Centre, 'Institute Computer Centre'),
    (HOBBIES_CLUB, 'Hobbies Club'),
    (INSTITUTE_COMPUTER_Centre, 'Institute Computer Centre'),
    (HOSPITAL_BOOKLET_CANCELLATION, 'Hospital Booklet Cancellation'),
    (INSTITUTE_SPORTS_ASSOCIATION, 'Institute Sports Association'),
    (THESIS_SUBMISSION_PROOF, 'Thesis Submission Proof'),
    (ALUMNI_MEMBERSHIP_PROOF, 'Alumni Membership Acknowledgement proof'),
    (BANK_ACCOUNT_DETAILS, 'Bank Account details'),
    (FINANCE_SECTION, 'Finance Section'),
    (ACADEMIC_SECTION, 'Academic Section'),
)
