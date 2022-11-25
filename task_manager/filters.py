from django_filters import FilterSet, BooleanFilter
from task_manager.models import task


class TaskFilter(FilterSet):

    class Meta:
        model = task
        fields = ['executor', 'status', 'labels', ]

    @property
    def qs(self):
        parent = super().qs
        if self.request.GET.get('self_tasks'):
            # print(self.request.GET)
            user = getattr(self.request, 'user')
            return parent.filter(creator=user)
        else:
            return parent
