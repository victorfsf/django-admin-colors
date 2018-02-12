from admincolors.site import AdminColorsSite
from django.test import TestCase


class TestAdminColorsSite(TestCase):

    def setUp(self):
        self.site = AdminColorsSite(name='test')

    def test_index_template(self):
        self.assertEqual(
            self.site.index_template,
            'admincolors/index.html'
        )
