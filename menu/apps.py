from django.apps import AppConfig


class MenuConfig(AppConfig):
    """
    Provides primary key type for menu app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
