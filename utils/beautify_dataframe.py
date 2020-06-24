import swapper
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from no_dues.models import Authority
from no_dues.constants import (PERMISSION_STATUS_DICTIONARY, APPROVED, 
    NOT_APPLICABLE, APPROVED_ON_CONDITION, NOT_REQUESTED, REPORTED, REQUESTED
)

PERMISSION_STATUS_DICTIONARY['nreq'] = 'Not Required'
Department = swapper.load_model('kernel', 'Department')
Centre = swapper.load_model('kernel', 'Centre')
department_id = ContentType.objects.get_for_model(Department).id
centre_id = ContentType.objects.get_for_model(Centre).id

authorities = Authority.objects.all()
all_authorities = list(authorities.values_list('full_name', flat=True))
departmental_authorities = list(authorities.filter(Q(slug__contains='_department') | Q(slug__contains='_centre')).values_list('full_name', flat=True))
bhawan_authorities = list(authorities.filter(slug__contains='_bhawan').values_list('full_name', flat=True))
mess_authorities = list(authorities.filter(slug__contains='_mess').values_list('full_name', flat=True))

def beautify_subscriber_dataframe(row):
    classname = Department
    if row['person__student__branch__entity_content_type_id'] == centre_id:
        classname = Centre
    row['Department'] = classname.objects.get(id=row['person__student__branch__entity_object_id']).name
    return row

def beautify_mass_dataframe(row):
    row['Department Status'] = PERMISSION_STATUS_DICTIONARY[row[row['Department']]]
    row['Final Status'] = 'All Approved, Not Applicable or Approved on Condition'
    row['Mess'] = ''
    bhawans=list()
    for column_name in all_authorities:
        try:
            if 'mess' in column_name and row[column_name]!='nreq':
                row['Mess'] = f'{column_name} - {PERMISSION_STATUS_DICTIONARY[row[column_name]]}'
            if 'bhawan' in column_name and row[column_name]!='nreq':
                bhawans.append(f'{column_name} - {PERMISSION_STATUS_DICTIONARY[row[column_name]]}')
            if row[column_name] in [NOT_REQUESTED, REPORTED, REQUESTED]:
                row['Final Status'] = 'Pending'
            row[column_name] = PERMISSION_STATUS_DICTIONARY[row[column_name]]
        except:
            pass
    row['Bhawan'] = bhawans
    return row

def delete_extra_columns(df):
    extra_column_names = departmental_authorities+bhawan_authorities+mess_authorities
    for column_name in extra_column_names:
        try:
            del df[column_name]
        except:
            pass
    return df