from django.apps import apps
from django.test import TestCase
from menu.apps import MenuConfig


class TestMenuConfig(TestCase):
    """Tests the Django app config."""
    def test_app(self):
        self.assertEqual('menu', MenuConfig.name)
        self.assertEqual('menu', apps.get_app_config('menu').name)