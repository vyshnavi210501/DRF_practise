import django_filters
from .models import Employee

class EmployeeFilters(django_filters.FilterSet):
    designation=django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    emp_name=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
    id_min=django_filters.CharFilter(method='filter_by_id',label='from empid')
    id_max=django_filters.CharFilter(method='filter_by_id',label='to empid')
    class Meta:
        model=Employee
        fields=['designation','emp_name','id_min','id_max']

    def filter_by_id(self,queryset,name,value):
        if name=='id_min':
            return queryset.filter(emp_id__gte=value)
        elif name=='id_max':
            return(queryset.filter(emp_id__lte=value))
        return(queryset)