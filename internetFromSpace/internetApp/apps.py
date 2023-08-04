from django.apps import AppConfig


class InternetappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'internetApp'

    def ready(self):
        import internetApp.signals