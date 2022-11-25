from django.test import TestCase, Client
from task_manager.models import status
from django.urls import reverse, reverse_lazy


class CRUD_Status_Test(TestCase):

    def setUp(self):
        status.objects.create(name='test_status')
        self.status = status.objects.get(id=1)

    def test_create_status(self):
        response = Client().post(reverse_lazy('status_create'), {'name': 'something'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that redirect url is rigth.
        self.assertRedirects(response, reverse_lazy('statuses_list'))

    def test_update_status(self):
        response = self.client.post(reverse('status_update', kwargs={'pk': self.status.pk}), {'name': 'test_status_2', })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses_list'))

    def test_delete_status(self):
        response = self.client.post(reverse('status_delete', kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses_list'))
