from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase

from blog import models, forms


class BlogViewsTest(TestCase):
    def setUp(self):
        self.user_one = User.objects.create_user(
            username='user_one', password='password_one')
        self.user_two = User.objects.create_user(
            username='user_two', password='password_two')

    def create_posts(self):
        post_one = models.Post.objects.create(
            author=self.user_one, title='qwerty_one', created_date=timezone.now())
        post_two = models.Post.objects.create(
            author=self.user_two, title='qwerty_two', created_date=timezone.now())
        post_one.publish()
        post_two.publish()
        return None

    def test_post_list_view(self):
        self.create_posts()
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['posts'], ['<Post: qwerty_two>', '<Post: qwerty_one>'])

    def test_user_post_list_view(self):
        self.create_posts()
        self.client.login(username='user_one', password='password_one')
        response = self.client.get(reverse('user_post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['user_posts'], ['<Post: qwerty_one>'])

    def test_post_detail_view(self):
        self.create_posts()
        post = models.Post.objects.get(author=self.user_one)
        response = self.client.get(reverse('post_detail', args=(post.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['post'], post)

    def test_post_new_view(self):
    	pass