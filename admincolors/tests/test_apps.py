from admincolors.apps import AdminColorsConfig
from django.test import TestCase


class TestAdminColorsConfig(TestCase):

    def test_name(self):
        self.assertEqual(
            AdminColorsConfig.name,
            'admincolors'
        )
