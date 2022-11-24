from django_filters import FilterSet, BooleanFilter
from task_manager.models import Task


class TaskFilter(FilterSet):

    def filter_creator(self, queryset, name, value):
        lookup = '__'.join([name, 'isnull'])
        return queryset.filter(**{lookup: False})

    class Meta:
        model = Task
        fields = ['executor', 'status', 'labels',]
