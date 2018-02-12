from admincolors.site import AdminColorsSite
from django.test import RequestFactory
from django.test import TestCase
from mock import MagicMock


class TestAdminColorsSite(TestCase):

    def setUp(self):
        self.site = AdminColorsSite(name='test')

    def test_index_template(self):
        self.assertEqual(
            self.site.index_template,
            'admincolors/index.html'
        )

    def test_each_context(self):
        request = RequestFactory().get('/admin/')
        request.user = MagicMock()
        context = self.site.each_context(request)
        self.assertEqual(context.get('themes'), [
            ('Default', ''),
            ('Test', 'test.css')
        ])
