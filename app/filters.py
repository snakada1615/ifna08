from django_filters import FilterSet
from django_filters import filters

from .models import FamilyList


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

class FamilyFilter(FilterSet):

    name = filters.ModelChoiceFilter(queryset = FamilyList.objects.all())
#    family_name = filters.CharFilter(label='family name', lookup_expr='contains')
#    women_s = filters.CharFilter(label='women special', lookup_expr='contains')

    order_by = MyOrderingFilter(

        fields=(
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels={
            'name': 'name',
            'age': 'age',
        },
        label='sort order'
    )

    class Meta:
        model = FamilyList
        fields = ('name',)
