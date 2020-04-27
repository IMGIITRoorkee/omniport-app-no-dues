from django_filters import FilterSet, MultipleChoiceFilter

from no_dues.models import Permission
from no_dues.constants import PERMISSION_STATUSES


class PermissionFilterSet(FilterSet):
    """
    Filterset for the Permission model
    """

    status = MultipleChoiceFilter(choices=PERMISSION_STATUSES)

    class Meta:
        """
        Meta class for the PermissionFilterSet
        """

        model = Permission
        fields = ['status']
