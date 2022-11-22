from django.test import TestCase, Client
from task_manager.models import User, Task, Status
from django.urls import reverse, reverse_lazy


class CRUD_Status_Test(TestCase):

    def setUp(self):
        User.objects.create_user(username='ivan_ivanov', password='qwerty')
        self.user = User.objects.get(id=1)
        Status.objects.create(name='status')
        self.status = Status.objects.get(id=1)
        Task.objects.create(name='task', description='something', creator=self.user, executor=self.user, status=self.status)
        self.task = Task.objects.get(id=1)

    def test_read_task(self):
        response = Client().get(reverse_lazy('task_view', kwargs={'pk': self.task.pk}), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        response = Client().post(reverse_lazy('task_create'), {'name': 'something'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that redirect url is rigth.
        self.assertRedirects(response, reverse_lazy('tasks_list'))

    def test_update_status(self):
        response = self.client.post(
            reverse('task_update', kwargs={'pk': self.task.pk}),
            {
                'name': 'new_task',
                'description': 'pass',
                'creator': 2,
                'executor': 2,
                'status': 2
            },
            follow=True
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_status(self):
        response = self.client.post(reverse('task_delete', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_list'))
