from django_filters import FilterSet, ModelMultipleChoiceFilter
from task_manager.models import task, label as label_model
from django.utils.translation import gettext_lazy as _


class TaskFilter(FilterSet):
    labels = ModelMultipleChoiceFilter(queryset=label_model.objects.all(), label=_('Label'), conjoined=True)

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
