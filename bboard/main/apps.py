from django.apps import AppConfig
from django.dispatch import Signal


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Доска объявлений'


user_registered = Signal(providing_args=['instance'])
