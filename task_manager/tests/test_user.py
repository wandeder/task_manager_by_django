from django.test import TestCase, Client
from task_manager.models import User
from django.urls import reverse, reverse_lazy


class CRUD_Users_Test(TestCase):

    def setUp(self):
        # Every test needs a user.
        User.objects.create_user(username='ivan_ivanov', password='qwerty')
        self.user = User.objects.get(id=1)

    def test_create_user(self):
        # Issue a POST request, create new user.
        response = Client().post(reverse_lazy('user_create'), {'username': 'john_smith', 'password': '12345'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that redirect url is rigth.
        # self.assertRedirects(response, reverse_lazy('user_create_done'))

    def test_read_user(self):
        response = self.client.post(reverse('login'), {'username': 'ivan_ivanov', 'password': 'qwerty'}, follow=True)
        user = User.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.is_authenticated, True)
        self.assertTemplateUsed(response, 'home.html')
        self.assertRedirects(response, reverse('home'))

    def test_update_user(self):
        self.client.login(username='ivan_ivanov', password='qwerty')
        response = self.client.post(reverse('user_update', kwargs={'pk': self.user.pk}),
                                    {'first_name': 'Ivan',
                                     'last_name': 'Ivanov',
                                     'email': 'ivanivanov@gmail.com'})
        self.assertEqual(response.status_code, 200)
        # print(response.context)
        # self.assertEqual(User.objects.get(id=1).first_name, 'Ivan')
        # self.assertEqual(self.user.last_name, 'Ivanov')
        # self.assertEqual(self.user.email, 'ivanivanov@gmail.com')

    def test_delete_user(self):
        self.client.login(username='ivan_ivanov', password='qwerty')
        response = self.client.post(reverse('user_delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users_list'))
