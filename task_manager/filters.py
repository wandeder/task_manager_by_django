from django_filters import FilterSet
from task_manager.models import task


class TaskFilter(FilterSet):

    class Meta:
        model = task
        fields = ['executor', 'status', 'labels', ]

    @property
    def qs(self):
        parent = super().qs
        if self.request.GET.get('self_tasks'):
            user = getattr(self.request, 'user')
            return parent.filter(creator=user)
        else:
            return parent
