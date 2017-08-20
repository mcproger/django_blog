from django.core.urlresolvers import reverse
from django.test import TestCase

from . import models


class BlogViewsTest(TestCase):
    def setUp(self):
        pass

    def get_queryset(self):
        return models.Post.objects.all()

    def test_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['posts'], self.get_queryset())
