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
 ('hlb_bhawan', 'Himalaya bhawan (Boys)'),
 ('hlg_bhawan', 'Himalaya bhawan (Girls)'),
 ('him_bhawan', 'Himgiri Apartment'),
 ('mvb_bhawan', 'Malviya bhawan'),
 ('rkb_bhawan', 'Radhakrishnan bhawan'),
 ('rjb_bhawan', 'Rajendra bhawan'),
 ('rgb_bhawan', 'Rajiv bhawan'),
 ('rvb_bhawan', 'Ravindra bhawan'),
 ('snb_bhawan', 'Sarojini bhawan'),
 ('kgb_bhawan', 'Kasturba bhawan'),
 ('igb_bhawan', 'Indira bhawan'),
 ('mar_bhawan', 'Married Hostels (G.P., M.R. Chopra, Azad Wing, D.S. Barrack, Vikas kunj)'),
 ('khs_bhawan', 'Khosla international house & A.N. Khosla house'),
 ('vigb_bhawan', 'Vigyan kunj (Boys)'),
 ('vigg_bhawan', 'Vigyan kunj (Girls)'),
 ('null_bhawan', 'Non-residing (No bhawan)')
]

# Mess
MESS_EDITED_SLUG = [('azb_mess', 'Azad bhawan mess'),
 ('ctb_mess', 'Cautley bhawan mess'),
 ('gnb_mess', 'Ganga bhawan mess'),
 ('gvb_mess', 'Govind bhawan mess'),
 ('jlb_mess', 'Jawahar bhawan mess'),
 ('rkb_mess', 'Radhakrishnan bhawan mess'),
 ('rjb_mess', 'Rajendra bhawan mess'),
 ('rgb_mess', 'Rajiv bhawan mess'),
 ('rvb_mess', 'Ravindra bhawan mess'),
 ('snb_mess', 'Sarojini bhawan mess'),
 ('kgb_mess', 'Kasturba bhawan mess'),
 ('mvigb_mess', 'Malviya & Indira bhawan mess'),
 ('vig_mess', 'Vigyan kunj mess'),
 ('hlg_mess', 'Himalaya bhawan mess'),
 ('null_mess', 'Non-dining (No mess)')
]

# Departments
DEPARTMENTS_EDITED_SLUG = [(f'{x[0]}_department', x[1].strip()) for x in DEPARTMENTS]

# Centres
CENTRES_EDITED_SLUG = [(f'{x[0]}_centre', x[1].strip()) for x in CENTRES]

# Clubs
NSS = 'nss'
NCC = 'ncc'
HEC = 'hec'
STUDENTS_TECHNICAL_COUNCIL = 'stc'
CULTURAL_COUNCIL = 'cuc'

CLUBS = (
    (NSS, 'National Service Scheme'),
    (NCC, 'National Cadet Corps'),
    (HEC, 'Himalayan Explorer\'s Club'),
    (STUDENTS_TECHNICAL_COUNCIL, 'Students Technical Council'),
    (CULTURAL_COUNCIL, 'Cultural Council')
)

# Other authorities
LIBRARY = 'lib'
CCB_OFFICE = 'ccb'
HOSPITAL_BOOKLET_CANCELLATION = 'hbc'
INSTITUTE_COMPUTER_Centre = 'icc'
INSTITUTE_SPORTS_ASSOCIATION = 'iso'
DORA_OFFICE = 'dor'
FINANCE_SECTION = 'fin'
ACADEMIC_SECTION = 'acad'
INSTITUTE_INSTRUMENTATION_CENTRE = 'iic'
SENATE_COMMITTEE_FOR_SCHOLARSHIP_AND_PRIZES_SCSP = 'scp'

OTHER_AUTHORITIES = (
    (LIBRARY, 'Central Library'),
    (CCB_OFFICE, 'CCB Office'),
    (INSTITUTE_COMPUTER_Centre, 'Institute Computer Centre'),
    (INSTITUTE_COMPUTER_Centre, 'Institute Computer Centre'),
    (HOSPITAL_BOOKLET_CANCELLATION, 'Hospital Booklet Cancellation'),
    (INSTITUTE_SPORTS_ASSOCIATION, 'Institute Sports Association & National Sports Organisation'),
    (DORA_OFFICE, 'DORA Office'),
    (FINANCE_SECTION, 'Finance Section'),
    (ACADEMIC_SECTION, 'Academic Section'),
    (INSTITUTE_INSTRUMENTATION_CENTRE, 'Institute Instrumentation Centre'),
    (SENATE_COMMITTEE_FOR_SCHOLARSHIP_AND_PRIZES_SCSP, 'Senate Committee for Scholarship and Prizes (SCSP)'),
)
