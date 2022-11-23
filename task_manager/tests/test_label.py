from django.test import TestCase, Client
from task_manager.models import Label
from django.urls import reverse, reverse_lazy


class CRUD_Status_Test(TestCase):

    def setUp(self):
        Label.objects.create(name='test_label')
        self.status = Label.objects.get(id=1)

    def test_create_status(self):
        # Issue a POST request, create new user.
        response = Client().post(reverse_lazy('label_create'), {'name': 'something'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that redirect url is rigth.
        self.assertRedirects(response, reverse_lazy('labels_list'))

    def test_update_status(self):
        response = self.client.post(reverse('labels_update', kwargs={'pk': self.status.pk}), {'name': 'test_label_2', })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_list'))

    def test_delete_status(self):
        response = self.client.post(reverse('label_delete', kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_list'))
