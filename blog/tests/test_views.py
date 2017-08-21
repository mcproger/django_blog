from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.test import TestCase

from blog import models


class BlogViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user', password='password')

    def get_posts_queryset(self):
        post = models.Post.objects.create(
            author=self.user, title='qwerty', created_date=timezone.now())
        post.publish()
        posts = models.Post.objects.all()
        return posts

    def test_post_list(self):
        posts = self.get_posts_queryset()
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['posts'], ['<Post: qwerty>'])
