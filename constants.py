from shell.constants.departments import DEPARTMENTS
from shell.constants.centres import CENTRES

# Permission statuses
NOT_REQUESTED = 'nrq'
REQUESTED = 'req'
REPORTED = 'rep'
NOT_APPLICABLE = 'nap'
APPROVED_ON_CONDITION = 'apc'
APPROVED = 'app'

PERMISSION_STATUSES = (
    (NOT_REQUESTED, 'Not Requested'),
    (REQUESTED, 'Requested'),
    (REPORTED, 'Reported'),
    (NOT_APPLICABLE, 'Not Applicable'),
    (APPROVED_ON_CONDITION, 'Approved On Condition'),
    (APPROVED, 'Approved'),
)

PERMISSION_STATUS_DICTIONARY = {
    NOT_REQUESTED: 'Not Requested',
    REQUESTED: 'Requested',
    REPORTED: 'Reported',
    NOT_APPLICABLE: 'Not Applicable',
    APPROVED_ON_CONDITION: 'Approved On Condition',
    APPROVED: 'Approved',
} 

# Residences
RESIDENCES_EDITED_SLUG = [('azb_bhawan', 'Azad bhawan'),
 ('ctb_bhawan', 'Cautley bhawan'),
 ('gnb_bhawan', 'Ganga bhawan'),
 ('gvb_bhawan', 'Govind bhawan'),
 ('jlb_bhawan', 'Jawahar bhawan'),
 ('mvb_bhawan', 'Malviya bhawan'),
 ('rkb_bhawan', 'Radhakrishnan bhawan'),
 ('rjb_bhawan', 'Rajendra bhawan'),
 ('rgb_bhawan', 'Rajiv bhawan'),
 ('rvb_bhawan', 'Ravindra bhawan'),
 ('snb_bhawan', 'Sarojini bhawan'),
 ('kgb_bhawan', 'Kasturba bhawan'),
 ('igb_bhawan', 'Indira bhawan'),
 ('mar_bhawan', 'Married Hostels (G.P., M.R. Chopra, Azad Wing, D.S. Barrack)'),
 ('khs_bhawan', 'Khosla international house & A.N. Khosla house'),
 ('vigb_bhawan', 'Vigyan kunj (Boys)'),
 ('vigg_bhawan', 'Vigyan kunj (Girls)')
]

# Mess
MESS_EDITED_SLUG = [('azb_mess', 'Azad bhawan mess'),
 ('ctb_mess', 'Cautley bhawan mess'),
 ('gnb_mess', 'Ganga bhawan mess'),
 ('gvb_mess', 'Govind bhawan mess'),
 ('jlb_mess', 'Jawahar bhawan mess'),
 ('mvb_mess', 'Malviya bhawan mess'),
 ('rkb_mess', 'Radhakrishnan bhawan mess'),
 ('rjb_mess', 'Rajendra bhawan mess'),
 ('rgb_mess', 'Rajiv bhawan mess'),
 ('rvb_mess', 'Ravindra bhawan mess'),
 ('snb_mess', 'Sarojini bhawan mess'),
 ('kgb_mess', 'Kasturba bhawan mess'),
 ('igb_mess', 'Indira bhawan mess'),
 ('vig_mess', 'Vigyan kunj mess')
]

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
DORA_OFFICE = 'dor'
BANK_ACCOUNT_DETAILS = 'bad'
FINANCE_SECTION = 'fin'
ACADEMIC_SECTION = 'acad'

OTHER_AUTHORITIES = (
    (LIBRARY, 'Central Library'),
    (CCB_OFFICE, 'CCB Office'),
    (INSTITUTE_COMPUTER_Centre, 'Institute Computer Centre'),
    (HOBBIES_CLUB, 'Hobbies Club'),
    (INSTITUTE_COMPUTER_Centre, 'Institute Computer Centre'),
    (HOSPITAL_BOOKLET_CANCELLATION, 'Hospital Booklet Cancellation'),
    (INSTITUTE_SPORTS_ASSOCIATION, 'Institute Sports Association'),
    (THESIS_SUBMISSION_PROOF, 'Thesis Submission Proof'),
    (DORA_OFFICE, 'DORA Office'),
    (BANK_ACCOUNT_DETAILS, 'Bank Account details'),
    (FINANCE_SECTION, 'Finance Section'),
    (ACADEMIC_SECTION, 'Academic Section'),
)
